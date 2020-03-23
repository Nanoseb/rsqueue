
import os
import subprocess
import re
import datetime
import xml.etree.ElementTree as ET
from itertools import islice


def get_job_info(jobID):
    """
        Get job raw job info in a dictionnary from a jobID thanks to scontrol call
    """
    jobInfo = {}

    output = subprocess.check_output(["scontrol", "show", "job", str(jobID)])
    for element in re.findall(r'[^\ ]*=[^\ ]*', output)
        key, content = element.split('=', 2)
        jobInfo[key] = content

    return jobInfo


def get_date(date_string):
    return datetime.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')


def get_duration(duration_string):
    duration_list = re.search(r'([0-9]*)-([0-9]{2}):([0-9]{2}):([0-9]{2})', duration_string).group()
    return datetime.timedelta(days=duration_list[0], hours=duration_list[1], minutes=duration_list[2], seconds=duration_list[3])

def head(f, lines=1):
    """
        Returns the first 'lines' lines of file 'f' as a list
    """
    return list(islice(f, lines))


def tail(f, lines=1):
    """
       Returns the last `lines` lines of file `f` as a list. (from https://stackoverflow.com/a/45960693)
    """
    if window == 0:
        return []

    BUFSIZ = 1024
    f.seek(0, 2)
    remaining_bytes = f.tell()
    size = window + 1
    block = -1
    data = []

    while size > 0 and remaining_bytes > 0:
        if remaining_bytes - BUFSIZ > 0:
            # Seek back one whole BUFSIZ
            f.seek(block * BUFSIZ, 2)
            # read BUFFER
            bunch = f.read(BUFSIZ)
        else:
            # file too small, start from beginning
            f.seek(0, 0)
            # only read what was not read
            bunch = f.read(remaining_bytes)

        #bunch = bunch.decode('utf-8')
        data.insert(0, bunch)
        size -= bunch.count('\n')
        remaining_bytes -= BUFSIZ
        block -= 1

    return ''.join(data).splitlines()[-window:]


def to_human(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)





class job:
    def __init__(jobID):
        self.jobID = jobID

        jobInfo = get_job_info(self.jobID)

        self.name = jobInfo['JobName']

        self.start_time  = get_date(jobInfo['StartTime'])
        self.submit_time = get_date(jobInfo['SubmitTime'])
        self.end_time    = get_time(jobInfo['EndTime'])
        self.time_limit  = get_duration(jobInfo['TimeLimit'])

        self.state       = jobInfo['JobState']
        self.reason      = jobInfo['Reason']
        self.stdout      = jobInfo['StdOut']
        self.num_core    = jobInfo['NumCPUs']
        self.working_dir = jobInfo['WorkDir']



    def get_ReFRESCO_info(self):
        self.controls_file       = os.path.join(self.working_dir, 'controls.xml')
        self.residuals_file      = os.path.join(self.working_dir, 'residuals.xml')
        self.counters_file       = os.path.join(self.working_dir, 'counters.xml')
        self.report_general_file = os.path.join(self.working_dir, 'report_general.xml')


        self.isReFRESCO = os.path.exists(self.controls_file) and \
                          os.path.exists(self.residuals_file) and \
                          self.state == 'RUNNING' # TODO test for ReFRESCO in stdout 

        if not self.isReFRESCO:
            return DDD

        # Opening files
        self.controls_tree = ET.parse(self.controls_file).getroot()
        self.report_general_tree = ET.parse(self.report_general_file).getroot()

        with open(self.counters_file, 'r') as counters:
            counters_last_line = [ float(x) for x in tail(counters, 1)[-1].split(None) ]
            counters_first_line = [ float(x) for x in head(counters, 3)[-1].split(None) ]


        unsteady = self.get_controls('controls/timeLoop/unsteady') == 'true'

        if unsteady:
            self.current_step = int(counters_last_line[1])
            self.initial_step = int(counters_first_line[1])
            self.max_step = int(self.get_controls("controls/timeLoop/maxTimesteps"))

            #initial_step = int(self.get_report_general("log/counters_info/start_time_step"))

            # [ ! "$initialtimestep" ] && initialtimestep=0

            #outer_max = int(self.get_controls("controls/outerLoop/maxIteration"))
            #outer_current = counters_last_line[2]
            #if outer_max == outer_current:
            #    outerwarn = "!"
        else:
            self.current_step = int(counters_last_line[0])
            self.initial_step = int(counters_first_line[0])
            self.max_step = int(self.get_controls("controls/outerLoop/maxIteration"))


        progress = (self.current_step - self.initial_step)/(self.max_step - self.initial_step)
        ETA_date = self.current_time + (self.max_step - self.current_step)*(self.current_time - self.start_time)/(self.current_step - self.initial_step)
        time_left = ETA_date - self.current_time 
        max_possible_step = (self.current_step - self.initial_step)*self.jobtimelimit/(self.current_time - self.start_time) + self.initial_step
    
        if show_storage:

    nowsize=$(du -s "$dir" | awk '{print $1}')
                ETAsize=$(bc <<<"($maxtimestep - $currentstep)*($nowsize)/($currentstep-$initialtimestepf)")
                ETAsizeh=$(convert_human $(bc <<<"$ETAsize+$nowsize"))
                nowsizeh=$(convert_human $nowsize)
                ETAsizetotal=$((nowsize + ETAsize + ETAsizetotal))
                currentsizetotal=$((nowsize + currentsizetotal))
                if [[ "$((10#$ETAday))" -ge 1 ]]
                then
                    ETA24hsize=$(bc <<<"$ETA24hsize + 86400*$nowsize*($currentstep-$initialtimestep)/(($currentstep-$initialtimestepf)*($nowepoch - $startepoch))")
                else
                    ETA24hsize=$((ETA24hsize + ETAsize))
                fi
            f







    def get_controls(self, path):
        return self.controls_tree.find(path).text
    
    def get_report_general(self, path):
        return self.report_general_tree.find(path).text


    def get_ETA(self):
        return self.start_time + (self.max_iteration - self.current_iteration)*(self.current_time - self.start_time)/(self.current_iteration - self.init_iteration)






































    
def getvalue_avg(elem):
    try:
        minvalue = float(elem.find('time/minvalue').text)/100
        avgvalue = float(elem.find('time/avgvalue').text)/100
        maxvalue = float(elem.find('time/maxvalue').text)/100
    except:
        minvalue = float(elem.find('time/value').text)/100
        avgvalue = float(elem.find('time/value').text)/100
        maxvalue = float(elem.find('time/value').text)/100
        
    try:
        ncalls = int(float(elem.find('ncalls/value').text))
    except:
        ncalls = 1
        
    return minvalue, avgvalue, maxvalue, ncalls

def get_time_function(comp, functionList):
    _, _, ncalls, totaltime = comp.get_time()
    
    report_perfFilename = comp.filename("report_performance.xml")
    try:
        report_perf = ET.parse(report_perfFilename).getroot()
    except: 
        raise ValueError('error when reading the file: ' + report_perfFilename) 
    
    root = "petscroot/timertree" #[@desc='Timings tree']"
    
    path = root + "/event[name='overset_calc_outit']"
    for function in functionList:
        path += "/events/event[name='" + function + "']"
        
    elems = report_perf.find(path)
    if elems == None:
        return [0,0,0]
    else:
        return [getvalue_avg(elems)[0]*totaltime/ncalls, getvalue_avg(elems)[1]*totaltime/ncalls, getvalue_avg(elems)[2]*totaltime/ncalls]






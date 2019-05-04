



class Job:
    def __init__(self, ID):
        self.ID = ID

        self.loadJobInfo()
        self.loadReFRESCOInfo()
        

    def loadJobInfo(self):
        # Ask slurm for all job info
        self.state = 
        self.path = 
        self.name = 
        self.core = 
        self.startTime =
        self.endTime = 

        self.stdoutFile =
        self.stderrFile = 

    def loadReFRESCOInfo(self):

        self.isReFRESCO = 

        # number of cells
        self.nCells = 

        self.isUnsteady = 

        # Time or outerloop related 
        #    initial is the begining of the current computation
        self.initialStep = 

        #    first step present in output files
        self.initialStepFile = 
        self.currentStep = 
        self.maxStep = 

        self.currentJobStorage = 

    def computeETA(self):

        self.etaTime = 
        self.etaSize = 
        self.etaStep = 
        self.etaCost = 



    

# rsqueue
Script used to monitor jobs and [refresco](http://www.refresco.org) running instances on slurm based clusters.
It has been first developed at MARIN (Maritime Research Institute Netherlands) hence some tweaking may be needed for other clusters.

## man : 
```
Usage: rsqueue [OPTIONS]
Outputs:
  -i, --info              Print detailed info about refresco job (default behaviour)
                               A "!" will appear near the "Iterations" column if the calculation is not converging
                               The time left will turn red if the runtime specified in the jobfile is not long enough
  -u, --user ([users])    Print job info of all users (default) or from a comma separated list of users
  -t, --top               Equivalent of slurmtop to summarize cluster load
  -p, --part              Print info about partitions usage
  -c, --count             Count the number of core used per user
  -a, --all               Print (almost) everything (equivalent of: rsqueue -u -t -p -i --progress-bar)

Output tweaking:
  -s, --storage           Print the storage needed for simulations (slows down the output)
  -r, --run               Print only running jobs
  --cost                  Print the current and final cost of the job 
  --memory                Print an estimation of the memory/core based on the cell count
  --maxit                 Print the maximum iteration number possible within the job time limit
  --st                    Sort job list by start time
  --pn                    Don't print the project number in the job name
  --node                  Print the nodes being used in the -u output
  --tree ([numdir]/all)   Print [numdir] number of subdirectories path in first column in a tree like form (default 2)
  --residuals             Print a detailed view of the residuals for each running computation
  --progress-bar          Print the computation progress graphically 

Tools:
  -d, --dir [jobID]       Print the working directory of the specified JobID
  --stop [jobID]          Write a stopfile in the computation working directory to cleanly stop the simulation
  -f, --follow ([time])   Refresh the your job list every [time]s (default being 15s)
  --notif                 Display a desktop notification when a job state changes, needs X-forwarding and -f
  --export-conf           Export a default configuration file in ~/.config/rsqueue.conf
  -v, --version           Show version number
  -h, --help              Print this help
```



# Rqstat

Equivalent of rsqueue for PBS/Torque clusters, this version is developed for Iridis4 (University of Southampton).

# Other
If you adapt this script for an other cluster please send it to me so that I can make it available for everyone

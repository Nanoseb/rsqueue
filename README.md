# Rsqueue
Script used to monitor jobs and refresco running instances more particularly on slurm based clusters.
It have been first develloped at MARIN (Maritime Research Institute Netherlands) so some parameters should be adapted for other facilities.

## man : 
```
Usage: rsqueue [OPTIONS]
Outputs:
  -i                       Print detailed info about refresco job (default behaviour)
                               A "!" will appear near the "Iterations" column if the calculation is not converging
                               The time left will turn red if the runtime specified in the jobfile is not long enough
  -u ([users])             Print job info of all users (default) or from a comma separated list of users
  -t / --top               Equivalent of slurmtop to summarize cluster load
  -p                       Print info about partitions usage
  -c                       Count the number of core used per user 
  -a / --all               Print (almost) everything (equivalent of: rsqueue -u -t -p -i)

Output tweaking:    
  -s                       Don't print the storage needed for simulations (speed up output)
  -r                       Print only running jobs
  --maxit                  Print the maximum iteration number possible within the job time limit
  --st                     Sort job list by start time
  --pn                     Don't print the project number in the job name
  --node                   Print the nodes being used in the -u output

Tools:
  -d [jobID]               Print the working directory of the specified JobID
  --stop [jobID]           Write a stopfile in the computation working directory to cleanly stop the simulation
  -f / --follow ([time])   Refresh the your job list every [time]s (default being 15s)
  -h / --help              Print this helps
```



# Rqstat

Equivalent of rsqueue for PBS/Torque clusters, this version is developed for Iridis4 (University of Southampton).

# Other
If you adapt this script for an other cluster please send it to me so that I can make it available for everyone

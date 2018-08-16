# Rsqueue
Script used to monitor jobs and refresco running instances more particularly on slurm based clusters.
It have been first develloped at MARIN (Maritime Research Institute Netherlands) so some parameters should be adapted for other facilities.

## man : 
<table>
  <tr>
    <td>-i</td>
    <td>Print detailed info about refresco job (default behaviour),A "!" will appear near the "Iterations" column if the calculation is not converging,The time left will turn red if the runtime specified in the jobfile is not long enough</td>
  </tr>
  <tr>
    <td>-u ([users])</td>
    <td>Print job info of all users (default) or from a comma separated list of users</td>
  </tr>
  <tr>
    <td>-t / --top</td>
    <td>Equivalent of slurmtop to summarize cluster load</td>
  </tr>
  <tr>
    <td>-p</td>
    <td>Print info about partitions usage</td>
  </tr>
  <tr>
    <td>-c</td>
    <td>Count the number of core used per user</td>
  </tr>
  <tr>
    <td>-d [jobID]</td>
    <td>Print the working directory of the specified JobID</td>
  </tr>
  <tr>
    <td>-s</td>
    <td>Don't print the storage needed for simulations</td>
  </tr>
  <tr>
    <td>-r</td>
    <td>Print only running jobs</td>
  </tr>
  <tr>
    <td>--st</td>
    <td>Sort job list by start time</td>
  </tr>
  <tr>
    <td>--pn</td>
    <td>Don't print the project number in the job name</td>
  </tr>
  <tr>
    <td>-a / --all</td>
    <td>Print (almost) everything (equivalent of: rsqueue -u -t -p -i)</td>
  </tr>
  <tr>
    <td>-h / --help</td>
    <td>Print this help</td>
  </tr>
</table>




# Rqstat

Equivalent of rsqueue for PBS/Torque clusters, this version is developed for Iridis4 (University of Southampton).

# Other
If you adapt this script for an other cluster please send it to me so that I can make it available for everyone

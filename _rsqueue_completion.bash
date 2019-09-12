#!/bin/bash
# Autocompletion script for rsqueue
# by Sebastien Lemaire <sebastien.lemaire@soton.ac.uk>
# license MIT

_rsqueue() 
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    #  Basic arguments to complete
    opts="--info -i --user -u --top -t --part -p --count -c --all -a --storage -s --run -r --cost --memory --maxit --st --pn \
          --node --tree --residuals --progress-bar -dir -d --stop --follow -f --notif --export-conf --version -v --help -h"


    #  Dynamic completion of arguments
    case "${prev}" in
        -d|--dir|--stop)
            local jobid=$(squeue -u $USER -o "%i" -h)

            COMPREPLY=( $(compgen -W "${jobid}" -- ${cur}) )
            return 0
            ;;
        -u|--user)
            local userlist=$(squeue -o "%u" -h | sort | uniq)

            COMPREPLY=( $(compgen -W "${userlist}" -- ${cur}) )
            return 0
            ;;
        -f|--follow)
            local timelist="5 15 30 120"

            COMPREPLY=( $(compgen -W "${timelist} ${opts}" -- ${cur}) )
            return 0
            ;;
        *)
            ;;
    esac

    COMPREPLY=($(compgen -W "${opts}" -- ${cur}))  
    return 0
}

complete -F _rsqueue rsqueue


# Function to move to a computation directory via its jobID
qcd () {
    local job_working_directory=$(rsqueue -d $1)
    if [ -d "$job_working_directory" ]
    then
        echo "Moving to $job_working_directory"
        cd "$job_working_directory"
    fi
}


_qcd()
{
    local cur jobid
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    jobid=$(squeue -u $USER -o "%i" -h)

    COMPREPLY=( $(compgen -W "${jobid}" -- ${cur}) )
    return 0
}

complete -F _qcd qcd 

#!/bin/bash
# Autocompletion script for rsqueue
# by Sebastien Lemaire <sebastien.lemaire@soton.ac.uk>
# license MIT

_rsqueue() {
    local cur prev opts
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    #  Basic arguments to complete
    opts="--info -i --user -u --top -t --part -p --count -c --all -a --storage -s --run -r --cost --memory --maxit --st --pn \
          --node --tree --residuals --progress-bar --dir -d --stop --follow -f --notif --export-conf --version -v --help -h"

    #  Dynamic completion of arguments
    case "${prev}" in
        -d|--dir|--stop)
            local jobid=$(squeue -u $USER -o "%i" -h)

            COMPREPLY=( $(compgen -W "${jobid}" -- ${cur}) )
            ;;
        -u|--user)
            local userlist=$(squeue -o "%u" -h | sort | uniq)

            COMPREPLY=( $(compgen -W "${userlist}" -- ${cur}) )
            ;;
        -f|--follow)
            local timelist="5 15 30 2m 5m"

            COMPREPLY=( $(compgen -W "${timelist} ${opts}" -- ${cur}) )
            ;;
        --tree)
            COMPREPLY=( $(compgen -W "1 2 3 5 all" -- ${cur}) )
            ;;
        *)
            COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )  
            ;;
    esac

    return 0
}

complete -F _rsqueue rsqueue


# jcd:
# Move to a job working directory from its jobID
jcd () {
    local job_working_directory=$(rsqueue -d ${1%%-*})
    if [ -d "$job_working_directory" ]
    then
        echo "Moving to $job_working_directory"
        cd "$job_working_directory"
    fi
}

_jcd() {
    local cur jobid
    cur="${COMP_WORDS[COMP_CWORD]}"
    jobid=$(squeue -u $USER -o "%i" -h)

    COMPREPLY=( $(compgen -W "${jobid}" -- ${cur}) )
    return 0
}

complete -F _jcd jcd 


# qcd:
# Wrapper of cd to move to a job working directory, autocompletion of only job directories
qcd () {
    if [ -d "${@: -1}" ]
    then
        cd "${@: -1}"
    fi
}

_qcd() {
    local cur paths
    local IFS=$'\n'

    # Output one suggestion per line
    local width=$(bind -v | sed -n 's/^set completion-display-width //p')

    if [[ $width -ne 0 ]]; then
        # change the readline variable
        bind "set completion-display-width 0"

        # set up PROMPT_COMMAND to reset itself to its current value
        PROMPT_COMMAND="PROMPT_COMMAND=$(printf %q "$PROMPT_COMMAND")"

        # set up PROMPT_COMMAND to reset the readline variable
        PROMPT_COMMAND+="; bind 'set completion-display-width $width'"
    fi

    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    case "${prev}" in
        -r|--running)
            paths=$(squeue -u $USER -o "%Z" -h -t RUNNING) 
            ;;
        -p|--pending)
            paths=$(squeue -u $USER -o "%Z" -h -t PENDING) 
            ;;
        *)
            paths=$(squeue -u $USER -o "%Z" -h)
            ;;
    esac


    COMPREPLY=( $(compgen -W "${paths}" -- ${cur}) )
    return 0
}

complete -F _qcd qcd


# Unload function definitions and autocompletion bindings
if [ "$1" = "unload" ]
then
    unset -f _rsqueue
    unset -f jcd
    unset -f _jcd
    unset -f qcd
    unset -f _qcd

    complete -A file rsqueue
    complete -A file jcd
    complete -A file qcd
fi


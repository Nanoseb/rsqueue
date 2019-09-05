#!/bin/bash
# Autocompletion script for rsqueue
# by Sebastien Lemaire <sebastien.lemaire@soton.ac.uk>
# license MIT

_rsqueue() 
{
    local cur prev opts base
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    #  Basic arguments to complete
    opts="-i --user --top --part --count -a --all --storage --run --cost --memory --maxit --st --pn --node --tree --residuals --progress-bar -d --stop --follow --notif --export-conf --version --help"


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

            COMPREPLY=( $(compgen -W "${timelist}" -- ${cur}) )
            return 0
            ;;
        *)
            ;;
    esac

    COMPREPLY=($(compgen -W "${opts}" -- ${cur}))  
    return 0
}

complete -F _rsqueue rsqueue

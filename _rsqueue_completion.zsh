#!/bin/bash
# Autocompletion script for rsqueue
# by Sebastien Lemaire <sebastien.lemaire@soton.ac.uk>
# license MIT


compdef _gnu_generic rsqueue


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

function _jcd(){
    _describe 'jcd' "($(squeue -u $USER -h -o "%i:%j\ %Z"))"   
}

compdef _jcd jcd 


# qcd:
# Wrapper of cd to move to a job working directory, autocompletion of only job directories
qcd () {
    if [ -d "${@: -1}" ]
    then
        echo "Moving to ${@: -1}"
        cd "${@: -1}"
    fi
}

_qcd() {
    _describe 'jcd' "($(squeue -u $USER -h -o "%Z:%i\ %j"))"   
}

compdef _qcd qcd


# Unload function definitions and autocompletion bindings
if [ "$1" = "unload" ]
then
    unset -f jcd
    unset -f _jcd
    unset -f qcd
    unset -f _qcd

    compdef _files rsqueue
    compdef _files jcd
    compdef _files qcd
fi


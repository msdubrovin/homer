#!/bin/bash

_OFNAME=~/test_crontab_1hour
echo "In ~/bin/cron_auto_proc.sh" >> ${_OFNAME}

#if [ -f /etc/profile ]; then
#  source /etc/profile
#fi

#if [ -f /etc/bashrc ]; then
#  source /etc/bashrc
#fi

if [ -f ~/.bash_profile ]; then
  source ~/.bash_profile &>> ${_OFNAME}
fi

_OFNAME=~/test_crontab_1hour

#rm ${_OFNAME}
date >> ${_OFNAME}

cd .../con-jungfrau

echo "HOSTNAME=$HOSTNAME" >> ${_OFNAME}
echo "LOGNAME=$LOGNAME" >> ${_OFNAME}
echo "HOME=$HOME" >> ${_OFNAME}
echo "PWD=$PWD" >> ${_OFNAME}

PATH=~/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin

#if [ -d $PWD/bin ]; then
#  PATH=$PWD/bin:$PATH
#fi

LD_LIBRARY_PATH=
PYTHONPATH=

. /reg/g/psdm/bin/conda_setup &>> ${_OFNAME}
#. /reg/g/psdm/bin/conda_setup 2>&1 >> ${_OFNAME}
#. conda_setup

#echo "PATH=$PATH" >> ${_OFNAME}
#echo "LD_LIBRARY_PATH=$LD_LIBRARY_PATH" >> ${_OFNAME}
echo "PYTHONPATH=$PYTHONPATH" >> ${_OFNAME}

export PATH
export LD_LIBRARY_PATH
export PYTHONPATH

#env >> ${_OFNAME}

bjobs -a -u $LOGNAME &>> ${_OFNAME}

#_MYSCRIPT="proc_new_datasets"
#_MYSCRIPT="proc_new_datasets -h"
_MYSCRIPT="proc_new_datasets -n 5 -s cspad,cspad2x2,pnccd,opal,epix100,zyla -S"

echo "Execute command: ${_MYSCRIPT}" >> ${_OFNAME}

${_MYSCRIPT} &>> ${_OFNAME}

#=======
exit 0
#=======

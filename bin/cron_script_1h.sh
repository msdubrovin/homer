#!/bin/bash

_OFNAME=~/test_crontab_1hour
echo "In ~/bin/cron_script_1h.sh" > ${_OFNAME}

#rm ${_OFNAME}
date >> ${_OFNAME}

#. ~/bin/cron_auto_proc.sh &>> ${_OFNAME}
#. ~/bin/cron_auto_proc.sh 2>&1 >> ${_OFNAME}

#======
exit 0
#======

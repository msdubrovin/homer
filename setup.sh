#!/bin/bash

RELDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#export PATH=$RELDIR/install/bin:${PATH}
# temporary, until we install psdaq binaries
#export PATH=$RELDIR/build/bin:${PATH}
#pyver=$(python -c "import sys; print(str(sys.version_info.major)+'.'+str(sys.version_info.minor))")
export PYTHONPATH=$RELDIR
echo  PYTHONPATH = $PYTHONPATH

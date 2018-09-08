#!/usr/bin python
#------------------------------

import sys
from utils import get_homedir, get_enviroment, get_hostname, get_cwd,\
                  get_login, str_tstamp,\
                  load_textfile, save_textfile

#------------------------------
__author__ = 'M. Dubrovin'

def namer() :
    return '.%s/.at/.%s/.%s'%\
        (get_login(), get_hostname(), sys._getframe().f_code.co_name)

def cwname() :
    return '%s.cw'%(namer().rsplit('.',1)[0])

def logname() :
    return '%s/logs/wan_ip_change_log' % get_homedir()

def load_list(fname) :
    ifname = '%s/%s' % (get_homedir(), fname)
    return load_textfile(ifname, verb=False).rstrip('\n').split(' ')

def get_ts_ip() :
    return load_list(namer())

def get_sa_cw() :
    flds = load_list(cwname())
    return '%s%s'%(flds[0],__author__.split(' ')[1].lower()), flds[1][::-1]

sa, cw = get_sa_cw()

def save_ts_ip(ip) :
    ts = str_tstamp(fmt='%Y-%m-%dT%H:%M:%S')
    ofname = '%s/%s' % (get_homedir(), namer())
    rec = '%s %s' % (ts, ip)
    save_textfile(rec, ofname, mode='w', verb=False)
    return rec

def add_record_to_log(rec) :
    save_textfile(rec, logname(), mode='a', verb=False)
    
#------------------------------

if __name__ == "__main__" :
    print('get_enviroment("PWD") : %s' % get_enviroment(env='PWD'))
    print('get_homedir()         : %s' % get_homedir())
    print('get_login()           : %s' % get_login())
    print('get_hostname()        : %s' % get_hostname())
    print('get_cwd()             : %s' % get_cwd())
    print('str_tstamp()          : %s' % str_tstamp(fmt='%Y-%m-%dT%H:%M'))
    print('namer()               : %s' % namer())
    print('cwname()              : %s' % cwname())
    sys.exit('END OF TEST')

#------------------------------

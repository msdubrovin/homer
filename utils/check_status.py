#!/usr/bin/python

#------------------------------
import logging
logger = logging.getLogger('__name__')

from namer import namer, cwname, get_ts_ip, save_ts_ip, sa, cw, add_record_to_log
from wan_ip import router_wan_ip
from send_email import send_email_v0
from utils import get_login
#------------------------------

def check_status(do_send=False) :
    ts, ip_old = get_ts_ip()
    # logger.debug('%s %s %s %s' % (ts, ip_old, sa, cw))
    ip = router_wan_ip()
    logger.info('Current WAN ip: %s' % ip)
    
    if ip == ip_old :
        logger.info('No changes')
        if do_send : logger.debug('Force to send e-mail for test purpose')
        else : return
        #=======================
    rec = save_ts_ip(ip)
    logger.info('ip has changed, email msg: %s'%rec)
    send_email_v0(msg='Update %s'%rec,
                  subject='Msg from %s'%get_login())
    add_record_to_log('%s\n' % rec)
    
#------------------------------

if __name__ == "__main__" :
    import sys
    tname = sys.argv[1] if len(sys.argv)>1 else '0'
    level, do_send = (logging.INFO, False) if tname == '0' else\
                     (logging.DEBUG, True)
    logging.basicConfig(format='%(levelname)s %(name)s %(message)s',\
                        level=level)
    check_status(do_send)

# logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s: %(message)s',\
#                        datefmt='%Y-%m-%dT%H:%M:%S',\
#                        level=logging.DEBUG)
                        #filename='example.log', filemode='w'
#    sys.exit('End of test')

#------------------------------

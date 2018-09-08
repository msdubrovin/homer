#--------------------

import logging
logger = logging.getLogger('__name__')

from requests import get
import re

SERVICES = ['http://myip.dnsomatic.com',\
            'http://icanhazip.com/',\
            'https://ipapi.co/ip/',\
            'https://api.ipify.org']

#--------------------

def response(ws='https://api.ipify.org') :
    return get(ws).text

#--------------------

def ip_from_response(resp) :
    lst = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', resp)
    return lst[0] if len(lst)>0 else None

#--------------------

def router_wan_ip() :
    for i,ws in enumerate(SERVICES) :
        resp = response(ws)
        ip = ip_from_response(resp)        
        if ip is not None :
            logger.debug('got ip: %s from service #%d: %s' % (ip,i,ws))
            return ip
    logger.debug('ip was not found in services %s' % str(SERVICES))
    return None

#--------------------

if __name__ == "__main__" :
  def test_request_timing() :
    from time import time
    print('in test_request_timing()')
    for i,ws in enumerate(SERVICES) :
        t0_sec = time()
        resp = response(ws).strip('\n')
        print('Service #%d %30s time=%.3f sec resp: %s' % (i, ws, time()-t0_sec, resp))

#--------------------

if __name__ == "__main__" :
    test_request_timing()

    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    print('Selected request: %s' % str(router_wan_ip()))

#--------------------
#--------------------
#--------------------

#import urllib2
#ip = urllib2.urlopen("http://whatismyip.org").read()

#import urllib2  
#req = urllib2.Request('http://icanhazip.com', data=None)  
#response = urllib2.urlopen(req, timeout=5)  

#import urllib2, json
#data = json.loads(urllib2.urlopen("http://ip.jsontest.com/").read())
#print data["ip"]

# WORKS # curl -s "https://ident.me"
#for python 3:
#import urllib.request
#ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

#import urllib2
#ip = urllib2.urlopen('https://ident.me').read()#.decode('utf8')

#--------------------

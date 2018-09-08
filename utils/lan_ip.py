#--------------------

def lan_ip() :
    """ Returns LAN ip like 10.0.1.123
    """
    import subprocess
    cmd = 'ip route list'
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    data = p.communicate()
    flds = data[0].split()
    return flds[flds.index('src')+1]

#--------------------

def lan_ip_v2() :
    """ Returns LAN ip like 10.0.1.123
    """
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

#--------------------

if __name__ == "__main__" :
    print('LAN ip v1: %s' % lan_ip())
    print('LAN ip v2: %s' % lan_ip_v2())

#--------------------

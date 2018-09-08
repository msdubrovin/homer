#!/usr/bin python
#----------------------------
"""
Usage::
    # Import
    from send_email import send_text_email

See:
    * :py:class:`send_email`
"""
#------------------------------
import logging
logger = logging.getLogger('__name__')

from namer import sa, cw

__domain__ = 'gmail.com'
_sa = '%s@%s' % (sa,__domain__)

#------------------------------

def smtp_sendmail(smsg, me, to) :
    """Sends e-mail via smtplib sendmail.
    """
    serv = 'smtp.%s'%__domain__
    #print _sa,me,to,cw,serv

    import smtplib
    s = smtplib.SMTP(serv, 587)
    s.ehlo()
    s.starttls()
    s.ehlo
    s.login(me,cw)
    s.sendmail(me, [to], smsg)
    s.quit()
    logger.debug('string message:\n====\n%s\n====' % smsg)    

#------------------------------

def send_email_v0(msg=None, subject=None, to=_sa) :
    """Sends e-mail.
    """
    header = 'To: %s\nFrom: %s\nSubject: %s' % (to,_sa,subject)
    smsg = '%s\n\n%s' % (header,msg)
    smtp_sendmail(smsg, _sa, to)

#------------------------------

def send_email_v1(msg=None, subject=None, to=_sa, cw=None) :
    """Sends e-mail.
    """
    from email.mime.text import MIMEText
    dmsg = MIMEText(msg)
    dmsg['Subject'] = str(subject)
    dmsg['From']    = _sa
    dmsg['To']      = to
    smsg = dmsg.as_string()
    smtp_sendmail(smsg, _sa, to)

#------------------------------

def send_email_v2(msg=None, subject='', to=_sa) :
    """Sends e-mail.
    """
    from subprocess import Popen, PIPE
    p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
    #p = Popen(["%s /usr/bin/mail", "-t", "-oi"], stdin=PIPE)

    p.communicate(smsg)
    logger.debug('submitted')

#------------------------------

if __name__ == "__main__" :
  def test_send_email() :
    print 20*'_', '\n%s:' % sys._getframe().f_code.co_name 
    send_email_v0(msg='Test message',
                  subject='Test subject', to=_sa)

#------------------------------

if __name__ == "__main__" :
    logging.basicConfig(format='%(levelname)s %(message)s',level=logging.DEBUG)
    import sys; global sys
    tname = sys.argv[1] if len(sys.argv) > 1 else '0'
    print 50*'_', '\nTest %s:' % tname
    if   tname == '0' : test_send_email()
    elif tname == '1' : test_send_email()
    else : print('Not-recognized test: %s' % tname)
    sys.exit('End of test %s' % tname)

#------------------------------

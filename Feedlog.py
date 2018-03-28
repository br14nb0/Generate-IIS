import socket
import sys
import time
from random import *
import datetime
import string

def randomIISlog():
    min_char = 3
    max_char = 9
    with open('E:/iplist.txt') as f:
    	tmp1 = f.read().splitlines()
    f.close()
    IPlist = [x.replace(' ', '%20') for x in tmp1]
    with open('E:/payload.txt') as g:
    	tmp2 = g.read().splitlines()	
    g.close()
    Payloadlist = [x.replace(' ', '%20') for x in tmp2]
    methodlist = ['GET', 'GET', 'GET', 'POST', 'POST', 'HEAD']
    URLlist = ['/tailieu', '/SitePages', '/_catalogs', '/_layouts', '/']
    userlist = ['HPTVIETNAM\quanth', 'HPTVIETNAM\luanpv', 'HPTVIETNAM\\nguyennc', 'HPTVIETNAM\\baovt', 'HPTVIETNAM\minhlc', '-', '-', '-' ]
    allchar = string.ascii_letters
    scstatuslist = ['200', '401', '304',]
    attacklist = ['<scRIpt>', 'alert', 'onLOad', 'svg', '</>', 'onerror', 'fromCharCode'\
	, 'select', 'union', 'InseRT']
    time = now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    method = ' '.join(sample(methodlist, 1))
    url = ' '.join(sample(URLlist, 1))
    attack = ' '.join(sample(attacklist, 1))
    ran = ''.join(choice(allchar) for x in range(randint(min_char, max_char)))
    payload = ' '.join(sample(Payloadlist, 1))
    query = ''.join(choice([payload, ran, ran, ran, ran]))
    iplocal = '10.0.'+str(randint(1,32)) + '.' + str(randint(1,24))
    ipglobal = ' '.join(sample(IPlist, 1))
    ip = ''.join(choice([iplocal,ipglobal]))
    username = ' '.join(sample(userlist, 1))
    scstatus = ' '.join(sample(scstatuslist, 1))
    scsubstatus = str(randint(0,3))
    scwin32status = str(randint(0,1000))
    bytesreceived = str(randint(1000,50000))
    bytessent = str(randint(1000,50000))
    timetaken = str(randint(200,2000))
    #      date time       s-ip            cs-method       s-uri-stem  cs-uri-query s-port  cs-username 
    return time + ' ' + '10.0.0.19 ' + method + ' ' + url + '/' + query + ' ' + ran + ' 443 ' + username + ' '\
    + ip + ' Mozilla/5.0+(Windows+NT+10.0;+WOW64;+Trident/7.0;+rv:11.0)+like+Gecko ' + scstatus + ' ' \
    + scsubstatus + ' ' + scwin32status + ' ' + bytesreceived + ' ' + bytessent + ' ' + timetaken

while(1):
	msg = randomIISlog()
	print(msg)
	time.sleep(2)
sys.exit(0)

'''
input{
	tcp{
		port => 7331
	}
}
'''

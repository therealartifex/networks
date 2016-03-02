#!/usr/bin/python

import ssl
import base64
from socket import *
from getpass import *

buf = 4096
m = raw_input('Message: ')
s = socket(AF_INET, SOCK_STREAM)
l = raw_input('Login: ')
p = getpass()

s.connect(("smtp-mail.outlook.com", 587))
print s.recv(buf)
s.sendall('ehlo selene.duckdns.org\r\n')
print s.recv(buf)
s.sendall('starttls\r\n')
print s.recv(buf)

ss = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv23)
ss.sendall('ehlo selene.duckdns.org\r\n')
print ss.recv(buf)
ss.sendall('auth login\r\n')
print ss.recv(buf)

ss.sendall(base64.b64encode(l)+'\r\n')
print ss.recv(buf)
ss.sendall(base64.b64encode(p)+'\r\n')
print ss.recv(buf)

ss.sendall('mail from:<linux.usaf@live.com>\r\n')
print ss.recv(buf)
ss.sendall('rcpt to:<linux.usaf@gmail.com>\r\n')
print ss.recv(buf)
ss.sendall('data\r\n')
print ss.recv(buf)

ss.sendall(m+'\r\n.\r\n')
print ss.recv(buf)
ss.sendall('quit\r\n')

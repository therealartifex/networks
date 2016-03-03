#!/usr/bin/python

# Brian Scott
# Programming Assignment 3 / "Tiny SMTP Client"
# COSC 3603-01 / "Networks and Data Communications"
# 
# This is a very simple SMTP client
# written in Python. It uses TLS through
# Microsoft's SMTP service.

# Development environment: vim on CentOS 7

import ssl
import base64
from socket import *
from getpass import *

buf = 4096
m = raw_input('Message: ')
r = raw_input("Recipient: ")
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
ss.sendall('rcpt to:<'+r+'>\r\n')
print ss.recv(buf)
ss.sendall('data\r\n')
print ss.recv(buf)

ss.sendall(m+'\r\n.\r\n')
print ss.recv(buf)
ss.sendall('quit\r\n')

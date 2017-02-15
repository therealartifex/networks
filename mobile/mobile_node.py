#!/usr/bin/python

# Brian Scott / Justin Largent
# COSC 4653 - Advanced Networks
# Assignment 3 - Mobile IP Simulation
# foreign_agent.py

# This simulates a mobile node in a mobile IP scenario

# Developed on Kali Linux 2
# Status: in development

import sys
from socket import *
from signal import *

ha_ip=sys.argv[1]
fa_ip=sys.argv[2]
co_ip=''

s=socket(AF_INET,SOCK_DGRAM)
s.bind(('',9000))

def sh(signal,frame):
  print('killing mobile node')
  s.close()
  sys.exit(0)
signal(SIGINT, sh)

def wait_for_msg():
  d,a=s.recvfrom(1024)
  f=d.split()
  print f[3]
  
while 1:
  print 'Choose:\n'
  print '1. Register\n'
  print '2. Deregister\n'
  print '3. Send message\n'
  c=raw_input()
  if c=='1':
    s.sendto('1 '+ha_ip+' '+ha_ip+' -',fa_ip)
    wait_for_msg()
  elif c=='2':
    s.sendto('2 '+ha_ip+' '+ha_ip+' -',fa_ip)
  elif c=='3':
    m=raw_input('Message: ')
    s.sendto('9 - - '+m,co_ip)


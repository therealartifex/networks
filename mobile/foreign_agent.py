#!/usr/bin/python

# Brian Scott / Justin Largent
# COSC 4653 - Advanced Networks
# Assignment 3 - Mobile IP Simulation
# foreign_agent.py

# This bla bla bla

# Developed on Kali Linux 2
# Status: in development

import sys
from socket import *
from signal import *

global mn_reg=0

s=socket(AF_INET,SOCK_DGRAM)
s.bind(('',8000))

def sh(signal,frame):
  print('killing mobile agent')
  s.close()
  sys.exit(0)
signal(SIGINT, sh)
print 'listening\n'

while 1:
  d,a=s.recvfrom(1024)
  f=d.split()
  print f

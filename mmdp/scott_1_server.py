#!/usr/bin/python

# Brian Scott
# COSC 4653 - Advanced Networks
# Assignment 1 - Min-Max-StdDev Distributed Processing
# scott_1_server.py

# This receives a set of random integers,
# calculates min, max and standard deviation,
# and sends it back to the client

# Developed on Kali Linux 2
# Status: working normally

import sys
from signal import *
from socket import *
import statistics

s=socket(AF_INET,SOCK_STREAM)
s.bind(('',int(sys.argv[1])))
s.listen(1)

c,adr=s.accept()

def sig_han(signal,frame):
  print('killing server')
  c.close()
  sys.exit(0)
signal(SIGINT, sig_han)

l=[]
while 1:
  msg=c.recv(64).strip()
  print msg
  if msg=="-1":
    break
  else:
    l.append(int(msg))
    
dat=[str(min(l)),str(max(l)),str(statistics.stdev(l))]
c.sendall(" ".join(dat))
c.close()
    


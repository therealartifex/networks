#!/usr/bin/python

# Brian Scott
# COSC 4653 - Advanced Networks
# Assignment 2 - Link-Layer Switch Simulation
# scottTS.py

# This reads a file containing a mock list of MAC addresses
# and interfaces, then sends data to a simulated switch containing
# a source MAC, destination MAC, and interface number. The script
# will send this data at random intervals and will run until killed.

# Developed on Kali Linux 2
# Status: finished

import random
from time import sleep
from sys import argv,exit
from signal import *
from socket import *

ival=int(argv[4])
s=socket(AF_INET,SOCK_DGRAM)
sw=(argv[1],int(argv[2]))

def sig_han(signal,frame):
  s.sendto('traffic stopped\n',sw)
  print('\nkilling traffic simulator')
  exit(0)
signal(SIGINT, sig_han)

d={}
mac=[]
with open(argv[3]) as f:
  for l in f:
    (k,v)=l.split()
    d[k]=int(v)
    mac.append(k)

while 1:
  wt=random.randrange(1,ival)
  rmac1=mac[random.randrange(0,len(mac)-1)]
  rmac2=mac[random.randrange(0,len(mac)-1)]
  sleep(wt)
  traf=str(d[rmac1])+' '+rmac1+' '+rmac2+'\n'
  s.sendto(traf.strip(),sw)
  print traf.strip()

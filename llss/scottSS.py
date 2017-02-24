#!/usr/bin/python

# Brian Scott
# COSC 4653 - Advanced Networks
# Assignment 2 - Link-Layer Switch Simulation
# scottSS.py

# This receives simultated traffic (MAC addresses) from another script
# and builds a switching table based on the incoming traffic.
# The switch simulator will print out information describing what
# action it takes depending on whether the MAC is in the table already,
# and whether or not the interface number matches the information
# in the switching table. The switch simulation script will run until
# it is killed.

# Developed on Kali Linux 2
# Status: finished

from time import sleep
from sys import argv,exit
from socket import *
from signal import *
from datetime import datetime

s=socket(AF_INET,SOCK_DGRAM)
s.bind(('',int(argv[1])))

def sig_han(signal,frame):
  print('\nkilling switch simulator')
  s.close()
  exit(0)
signal(SIGINT, sig_han)

table_max=int(argv[2])
age_max=int(argv[3])

d={}
while 1:
  data,a=s.recvfrom(256)
  data=data.strip()
  print data
  if data=='traffic stopped':
    s.close()
    exit(0)
  else:
    i,src,dest = data.split()
    mark_time = datetime.now()
    
    # step 1
    if src in d:
      d[src] = (mark_time,d[src][1])
      print "UPD"
    else:
      if len(d)<table_max:
        d[src] = (mark_time,i)
        print "ADD: Adding MAC '"+src+"' on iface '"+str(i)+"' to switch table"
      else:
        print "WARN: Could not add MAC '"+src+"' on iface '"+str(i)+"' to switch table"
    
    # step 2
    if dest not in d:
      print "BCST: Broadcasting frame w/ MAC '"+src+"'"
    else:
      if i==d[dest][1]:
        print "DISC: Discarding frame w/ MAC '"+src+"'"
      else:
        print "FWD: Forwarding frame w/ MAC '"+src+"' to iface '"+str(d[dest][1])+"'"
        
        
    # step 3
    for k in d.keys():
      if (datetime.now()-d[k][0]).seconds > age_max:
        print "DEL: " + str(d.pop(k,None))
      
    







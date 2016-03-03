#!/usr/bin/python

# Brian Scott
# COSC 3603-01 / "Networks and Data Commmunications"
# 30 Sept 2015
# Assignment 2 - "UDP Ping Client"

# This program is a small UDP client that
# simulates a ping to a server, with timeout handling.

# Development environment: vim on Debian 8


from socket import *
from datetime import datetime
import time

s = socket(AF_INET,SOCK_DGRAM)

for i in range(1,11):
  c = time.clock()
  s.sendto("Ping " + str(i) + " " + str(datetime.now().time()), ('127.0.0.1', 12000))
  s.settimeout(1.0)
  try:
    dat,adr = s.recvfrom(1024)
    e = time.clock() - c
    print "Response: %s\tRTT: %s ms\n" % (dat.strip(),e*1000)
  except error:
    print "Request timed out\n"

s.close()


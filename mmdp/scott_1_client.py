#!/usr/bin/python

# Brian Scott
# COSC 4653 - Advanced Networks
# Assignment 1 - Min-Max-StdDev Distributed Processing
# scott_1_client.py

# This splits a set of random integers
# into three subsets and sends them to 
# three servers, where various statistical
# information is calculated and returned to
# the client

# Developed on Kali Linux 2
# Status: working except for wrong formula for combined stddev

from socket import *
import random
import statistics
import sys
import numpy.random as nprnd
from time import sleep
import math

n=int(sys.argv[1])
s1adr=sys.argv[2]
s1prt=int(sys.argv[3])
s2adr=sys.argv[4]
s2prt=int(sys.argv[5])
s3adr=sys.argv[6]
s3prt=int(sys.argv[7])

s1=socket(AF_INET,SOCK_STREAM)
s2=socket(AF_INET,SOCK_STREAM)
s3=socket(AF_INET,SOCK_STREAM)

vals=nprnd.randint(1,1000000,size=n)

s1.connect((s1adr,s1prt))
s2.connect((s2adr,s2prt))
s3.connect((s3adr,s3prt))

for i in range(0,n):
  if i%3==1:
    s1.send(str(vals[i]))
  elif i%3==2:
    s2.send(str(vals[i]))
  elif i%3==0:
    s3.send(str(vals[i]))
  sleep(0.05)

s1.send("-1")
s1dat = s1.recv(1024).split()
sleep(0.05)

s2.send("-1")
s2dat = s2.recv(1024).split()
sleep(0.05)

s3.send("-1")
s3dat = s3.recv(1024).split()
sleep(0.05)

s1.close()
s2.close()
s3.close()

tmin=min(int(s1dat[0]),int(s2dat[0]),int(s3dat[0]))
tmax=max(int(s1dat[1]),int(s2dat[1]),int(s3dat[1]))
combine=(float(s1dat[2])**2)+(float(s2dat[2])**2)+(float(s3dat[2])**2)
print combine
tstdev=math.sqrt(combine/(n-1))

print("Results computed by the client from data sent by the server:")
print("Minimum value: "+str(tmin))
print("Maximum value: "+str(tmax))
print("Standard deviation value: "+str(tstdev)+"\n")

print("Results computed only by the client:")
print("Minimum value: "+str(min(vals)))
print("Maximum value: "+str(max(vals)))
print("Standard deviation value: "+str(statistics.stdev(vals)))



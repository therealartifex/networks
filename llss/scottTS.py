#!/usr/bin/python

import random
from time import sleep
from sys import argv
from socket import *


ssip=argv[1]
sspn=int(argv[2])
ival=int(argv[4])

d={}
with open(argv[3]) as f:
   for l in f:
      (k,v)=l.split()
      d[k]=int(v)

print d

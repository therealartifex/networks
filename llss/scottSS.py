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
# Status: unfinished

from time import sleep
from sys import argv
from socket import *

s=socket(AF_INET,SOCK_DGRAM)

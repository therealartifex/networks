###############
#Author: Justin Largent
#Assignment: Mobile IP Simulation
#
#
###############

from socket import *
import sys

socket = socket(AF_NET, SOCK_DGRAM);

#get IPs from command line
homeIP = sys.argv[1]
correspondentIP = sys.argv[2]

#port for the correspondent to listen on
correspondentPort = 6000



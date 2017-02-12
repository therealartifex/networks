#Authors: Justin Largent / Brian Scott
#Assignment: Mobile IP Simulation
#COSC4653 - Advanced Networks
#

from socket import *
import sys

socket = socket(AF_NET, SOCK_DGRAM);
socket.setdefaulttimeout(5)
#get IPs from command line
homeIP = sys.argv[1]
correspondentIP = sys.argv[2]

#port for the correspondent to listen on
correspondentPort = 6000

while 1:
	socket.settimeout()
	messageRecv1 = socket.recvfrom(1024).split()
	if(messageRecv1[0] == "9"):
		print "Message from mobile node: " + messageRecv1[1]
	
	options = raw_input("Chose either (1) Send a message or (2) shutdown: ")
	if(options == "1" || "send a message"):
		message = raw_input("Enter your message: ")
		socket.sendto(str(5) + " " + correspondentIP + " " + homeIP + " " + message)
		messageRecv2 = socket.recvfrom(1024).split()
		if(messageRecv2[0] == "6"):
			print "No mobile node with " + messageRecv2[1] + " is registered with the Home agent."
	if(options == "2" || options == "shutdown"):
		socket.sendto(str(0))
		break
socket.close()
#Authors: Justin Largent / Brian Scott
#Assignment: Mobile IP Simulation
#COSC4653 - Advanced Networks
#

from socket import *
import sys

sock = socket(AF_NET, SOCK_DGRAM);
sock.setdefaulttimeout(5)
#get IPs from command line
homeIP = sys.argv[1]
correspondentIP = sys.argv[2]

#port for the correspondent to listen on
correspondentPort = 6000
homePort = 7000

while 1:
	sock.settimeout()
	messageRecv1 = socket.recvfrom(1024).split()
	if(messageRecv1[0] == "9"):
		print "Message from mobile node: " + messageRecv1[1]
	
	options = raw_input("Chose either (1) Send a message or (2) shutdown: ")
	if(options == "1" or options == "send a message"):
		message = raw_input("Enter your message: ")
		sock.sendto(str(5) + " " + correspondentIP + " " + homeIP + " " + message, (homeIP, homePort))
		messageRecv2 = sock.recvfrom(1024).split()
		if(messageRecv2[0] == "6"):
			print "No mobile node with " + messageRecv2[1] + " is registered with the Home agent."
	if(options == "2" or options == "shutdown"):
		sock.sendto(str(0), (homeIP, homePort))
		break
sock.close()
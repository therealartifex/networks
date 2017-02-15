#Authors: Justin Largent / Brian Scott
#Assignment: Mobile IP Simulation
#COSC4653 - Advanced Networks
#

from socket import *
import sys

sock = socket(AF_INET, SOCK_DGRAM);
#get IPs from command line
homeIP = sys.argv[1]
correspondentIP = sys.argv[2]

#port for the correspondent to listen on
correspondentPort = 6000
homePort = 7000

while 1:
	sock.settimeout(5)
	try:
		messageRecv1, addr = sock.recvfrom(1024).split("\n")
		if(messageRecv1[0] == "9"):
			print "Message from mobile node: " + messageRecv1[1]
	except timeout:
		options = raw_input("Chose either (1) Send a message or (2) shutdown: ")
		if(options == "1" or options == "send a message"):
			message = raw_input("Enter your message:\n")
			sock.sendto(str(5) + "\n" + correspondentIP + "\n" + homeIP + "\n" + message, (homeIP, homePort))
			try:
				messageRecv2, addr = sock.recvfrom(1024).split("\n")
				if(messageRecv2[0] == "6"):
					print "No mobile node with " + messageRecv2[1] + " is registered with the Home agent."
			except timeout:
				continue
		if(options == "2" or options == "shutdown"):
			sock.sendto(str(0)+ "\n", (homeIP, homePort))
			break
sock.close()

#Authors: Justin Largent / Brian Scott
#Assignment: Mobile IP Simulation
#COSC4653 - Advanced Networks
#

from socket import *

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 7000))

mobileNodes = {}

while 1:
	messageRecv = socket.recvfrom(1024)
	message = messageRecv.split()
	if(message[0] == "0"):
		print "Shutting down"
		break
	if(message[0] == "3"):
		mobileNodes[message[2]] = message[1]
	if(message[0] == "4"):
		del mobileNodes[message[2]]
	if(message[0] == "5"):
		if(mobileNodes.has_key(message[2])):
			sock.sendto(str(7) + " " + message[1] + " " + mobileNodes[message[2]]+ " " + message[3], (mobileNodes[message[2]], 8000))
		else:
			sock.sendto(str(6) + " " + message[2], (message[1], 6000))
sock.close()
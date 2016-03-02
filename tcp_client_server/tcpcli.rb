#!/usr/bin/ruby

# Brian Scott
# COSC 3603-01 / "Networks and Data Communications"
# 12 Sept 2015
# Assignment 1 - "Web Server"

# This program is a simple TCP client
# written in Ruby, using sockets programming.
#
# Development Environmant: vim on CentOS 7
 

require 'socket'
host, port, obj = ARGV # command line arguments

s = TCPSocket.new(host, port) # connect to the specified host and port

s.print "#{obj.chomp}\r\n\r\n" # write the request with two CRLFs 
resp = s.read # read from the socket
puts resp # write to stdout

s.close

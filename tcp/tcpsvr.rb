#!/usr/bin/ruby

# Brian Scott
# COSC 3603-01 / "Networks and Data Communications"
# 12 Sept 2015
# Assignment 1 - "Web Server"
#
# This program is a simple TCP web server
# written in Ruby, using sockets programming.
#
# Development Environment: vim on CentOS 7

require 'socket'
require 'uri'

sock = TCPServer.open(9981)

# this turns a GET request into a relative path
def get_object(o)
   p = URI.unescape(URI(o.split(" ")[1]).path)
   return File.join('./',p) # join on the current directory
end

def conn_handler(c)
   the_time = "The current time is #{Time.now}\n"
   req = c.gets # read first line from client
   obj = get_object(req)
   STDERR.puts "Request from client #{c}: #{req}\n" # this is written to the server's stderr so it will be logged
   c.print the_time

   if File.exist?(obj) && !File.directory?(obj)
      File.open(obj, "rb") do |f|
         c.print "HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: #{f.size}\r\nConnection: close\r\n\r\n"
         IO.copy_stream(f,c)         
      end
   else
      m = "Object not found\n"
      c.print "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\nContent-Length: #{m.size}\r\nConnection: close\r\n\r\n"
      c.print m
   end
   
   c.close
end

STDERR.puts "Listening on port 9981. ^C to halt server."

while client = sock.accept
   Thread.new { conn_handler(client) } # new client? new thread!
end

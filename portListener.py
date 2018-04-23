#!/usr/bin/python
# PortListener
# by m0ses
# v1.1

import socket

print "    ___           _       __ _     _                       "
print "   / _ \___  _ __| |_    / /(_)___| |_ ___ _ __   ___ _ __ "
print "  / /_)/ _ \| '__| __|  / / | / __| __/ _ \ '_ \ / _ \ '__|"
print " / ___/ (_) | |  | |_  / /__| \__ \ ||  __/ | | |  __/ |   "
print " \/    \___/|_|   \__| \____/_|___/\__\___|_| |_|\___|_|   "
print
print " =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= "
print ">>>>>>>>>>>>>>>>>>>>>>>>>> m0ses <<<<<<<<<<<<<<<<<<<<<<<<<<"
print

ip = raw_input(">> Type IP adress: ")
port = input(">> Type port number: ")

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if sckt.connect_ex((ip, port)):
	print "[i] Port", port, "is close for", ip
	exit

else:
	print "[i] Port", port, "is open for", ip











# "Moses also heard voices"
# by m0ses

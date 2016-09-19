#encoding: utf-8
#!/usr/bin/python

import socket

HOST='127.0.0.1'
PORT=8000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect((HOST,PORT))
while 1:
       cmd=raw_input("坐标")
       s.sendall(cmd)
       data=s.recv(1024)
       from time import sleep
       sleep(0.2)

s.close()
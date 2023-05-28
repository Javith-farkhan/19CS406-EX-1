#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
s=socket.socket()
s.connect(('localhost',8080))
while True:
	print(s.recv(1024).decode())
	s.send("Recieved".encode())


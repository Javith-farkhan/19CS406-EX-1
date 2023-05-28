#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
s=socket.socket()
s.bind(('localhost',8080))
s.listen(5)
c,addr=s.accept()
while True:
   i=input("ENter a data:")
   c.send(i.encode())
   ack=c.recv(1024).decode()
   if ack:
   	print(ack)
   	continue
   else:
   	c.close()
   	break


# In[ ]:





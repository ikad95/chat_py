#!/usr/bin/python3
#use python 3.x for compatibility
#not tested with python 2.x
#ikad inc
import socket #import the socket module
import sys
import os
name = input('Your Nick : ')
def send_msg(c,s):
	str=input("")
	if str=='exit':
		c.close()
		s.close()
		sys.exit()
	str= '<'+name+'> '+str
	c.sendall(bytes(str,'UTF-8'))
	
def recv_n_brdcst_msg(c,addr):
	m=c.recv(4096)
	#m=m.decode('utf-8')
	m="<"+str(addr[0],'UTF-8')+":"+bytes(addr[1],'UTF-8')+"> "+m	
	sendall(m)
	print(m)


s_port = int(input('server port # '))
pid = os.fork()
if(pid==0):
	s = socket.socket() #Create a socket object
	s_host = ''  #Get the local machine name
	s.bind((s_host,s_port)) #Bind to the port read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
	s.listen(20) #Wait for the client connection
	c,addr = s.accept() #Establish a connection with the client
	while True:
		send_msg(c,s)
	exit(1)
else:
	c_port = int(input('client port # '))
	s = socket.socket() #create a socket object
	c_host = input('client ip # ')
	host =''
	s.connect((c_host,c_port))
	while True:
		m=s.recv(4096).decode("utf-8")
		if m=='exit':
			s.close()
			exit(1)
		else:
			print(m)
	s.close()

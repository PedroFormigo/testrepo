#App client

from socket import *

serverName = '194.210.193.75'
serverPort = 2000

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

request = 'GET / HTTP/1.1\r\nHost:194.210.193.75\r\n\r\n'
clientSocket.send(request.encode())
response = clientSocket.recv(1024).decode()
print(response)


clientSocket_2 = socket(AF_INET,SOCK_STREAM)
clientSocket_2.connect((serverName,serverPort))

request_2 = 'GET /ola.html HTTP/1.1\r\nHost:194.210.193.75\r\n\r\n'
clientSocket_2.send(request_2.encode())
response_2 = clientSocket_2.recv(1024).decode()
print(response_2)

clientSocket_3 = socket(AF_INET,SOCK_STREAM)
clientSocket_3.connect((serverName,serverPort))

request_3 = 'GET / HTTP/2.0\r\nHost:194.210.193.75\r\n\r\n'
clientSocket_3.send(request_3.encode())
response_3 = clientSocket_3.recv(1024).decode()
print(response_3)



#close Socket
clientSocket.close()

import time
import socket



    
port = 5000  # socket server port number

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
client_socket.connect(('127.0.0.1', port))  # connect to the server

message = input(" -> ")  # take input

client_socket.send(message.encode())  # send message
timer = int(5)
while(timer != 0):
    timer = timer-1
    time.sleep(1)
    print('continue waiting........')
            
            
    
ack = client_socket.recv(1024).decode()
print('ack from server: ' + ack)

data = client_socket.recv(1024).decode()  # receive response
print('messege from server: ' + data)  # show in terminal
ack = 'recieved'
client_socket.send(ack.encode())


client_socket.close()  # close the connection




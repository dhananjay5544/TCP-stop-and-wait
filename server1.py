import time
import socket



    
port = 5000  # initiate port no above 1024

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # get instance
    # look closely. The bind() function takes tuple as argument
server_socket.bind(('', port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
server_socket.listen(2)
print("waiting for incomming connections........")
conn, address = server_socket.accept()  # accept new connection
print("Got Connection from: " + str(address))
while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
    data = conn.recv(1024).decode()
    print("messege from client: " + str(data))
    ack='received'
    conn.send(ack.encode())
        
    data = input(' -> ')
    conn.send(data.encode())    # send data to the client
    timer=int(5)                #wait for 5 sec
    while (timer != 0 ):
        timer = timer-1
        time.sleep(1)
        print("continue waiting.........")
    ack = conn.recv(1024).decode()
    print('ack from client: ' + ack)

conn.close()  # close the connection








'''import time

timer=int(5)
while (timer != 0 ):
    timer=timer-1
    time.sleep(1)
    print(timer)
'''

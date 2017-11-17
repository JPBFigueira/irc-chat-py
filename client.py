import sys
import socket
import select


if(len(sys.argv)<3):
    print ('python client.py hostname port')
    sys.exit()

host = sys.argv[1]
port = int (sys.argv[2])

#socket tcp
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.settimeout(2)

try:
    clientSocket.connect((host, port))
except:
    print ('Failed to connect')
    sys.exit()


name = raw_input('enter name pls: \n')
clientSocket.send(name)
rcv = clientSocket.recv(1024)
print(rcv)
clientSocket.close()

import sys
import socket
import select
BUFFER = 1024
HOST = 'localhost'
PORT = 9000

def send_server(conn, addr):
    try:
        while True:
            msg = raw_input()
            conn.sendall(msg)

def recv_server(conn, addr):
    while True:
        msg = conn.recv(BUFFER)
        print msg


def main():
    #socket tcp
    clientSocket = socket(AF_INET, SOCK_STREAM)
    try:
        clientSocket.connect((host, port))
    except:
        print ('Failed to connect')
        sys.exit()

    recvt = Thread(target=recv_server, args=(clientSocket, HOST)
    recvt.start()
    print('enter username\n')
    send_server(clientSocket, HOST)
    print('enter destination ')
    send_server(clientSocket, HOST)

    while(1):
        print('enter msg')
        send_server(clientSocket, HOST)

    clientSocket.close()

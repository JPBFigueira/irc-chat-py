import socket
import sys
from sys import argv                                #IMPORT LIBRARIES
from threading import Thread
import Queue
HOST = 'localhost'
PORT = 9000
BUFFER = BUFFER

def __main__:

    activeUsers = []
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    activeUsers.append(serverSocket)
    print('ServerSocket created\n')
    try:
        serverSocket.bind((HOST,PORT))
    except socket.error as msg:
        print('failed binding\n')
        sys.exit()
    print('binded\n')
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    inputs = [serverSocket]
    outputs = []
    messages = {}
    serverSocket.listen(10)
    print('Listening\n')

    while(True):
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ' -> ' + str(addr[1]), end = ' ')
        thread = Thread(target=cthread, args=(conn, addr))   #Start a thread & connect
        thread.start()
#envia mensagens

def broadcast_data(sock, message):
    for socket in activeUsers:
        if socket !=server_coket and socket != sock:
            try:
                socket.send(message)
            except:
                print('not only tho\n')
                socket.close()
                activeUsers.remove(socket)
#criar ficheiro de cont
def cthread(conn):
    conn.send("hey bro") #TODO encode info?
    while True:
        user = conn.recv(BUFFER)
        user.append(activeUsers)
        createAcc(user)
        if(already_logged):
            print('already logged\n')
            conn.close()

        conn.send('gj nice user name '+ user + '\n')
        dest = conn.recv(BUFFER)
        while True:
            message = conn.recv(BUFFER)
            if dest in activeUsers:
                send_msg(user, dest, msg)
            else:
                conn.send('not online\n')

def createAcc(user):
    file = open(user, 'w+')
    f.close()

def already_logged(user):
    for user in activeUsers:
        if user[0] == user:
            return True
    return False

def broadcast(user):
    message = 'Message from ' + user ': '
    for user_tuple in activeUsers:
        user_tuple[1].sendall(message)

def send_msg(username, dest, msg):
    f = dest + 'txt'
    file = open(f, 'w+')
    f.writelines(user +'\n' +msg + '\n' + '-' + '\n')
    f.close()

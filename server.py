import socket
import sys
import collections
import time
import queue
import threading
from threading import Thread
from socketserver import ThreadingMixIn
HOST = 'localhost'
PORT = 9000
BUFFER = 1024

class ClientThread(Thread):
    def __init__(self, socket, ip, port):
        Thread.__init__(self)
        self.socket = socket
        self.ip = "127.0.0.1"
        self.port = 9999
        print ("hey")

    def run(self):
        while True:
            #logging in and appending username and userfd
            self.socket.send('how u doin')
            lock.acquire()
            user_name = self.socket.recv(1024)
            activeUsers.append(user_name)
            lock.release()
            print (user_name + "logged in\n")
            online = 1
            fd = self.socket.fileno()
            userfd = user_name + " " + str(fd)
            lock.aquire()
            userfdmap.append(userfd)
            lock.release()
            while True:
                command = self.socket.recv(BUFFER)
                if "send" in command:
                    content = command.partition(" ")
                    contentinner = content[2].partition(" ")
                    sendmsg = userdata + ": " + contentinner[2]
                    receiver = contentinner[0]
                    online = 1

                    for z in userfdmap:
                        zi=z.partition(" ")
                        if zi[0] == receiver:
                            receivefd = int(zi[2])
                            online =0
                            lock.acquire()
                            sendqueues([receiverfd].put(sendmsg))
                            lock.release()

                    if online == 1:
                        replymsg = 'User offline\n'
                        filename = receiver + '.txt'
                        file = open(filename, "a+")
                        file.write(sendmsg)
                        file.write('\n')
                        file.close()
                    else:
                        replymsg = 'sucess'
                        self.socket.send(replymsg)




class ClientThreadRead(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.sock = sock

    def run(self):
        tcpsock2.listen(1)
        (conn2,addr) = tcpsock2.accept()
        welcomemsg = "hi here hearing ya"
        conn2.send(welcomemsg)
        chat = "initial"
        #check if user is connected
        while True:
            for p in userfdmap:
                if str(self.sock.fileno()) in p:
                    connected = 1
                else:
                    connected = 0

                try:
                    chat = sendqueues[self.sock.fileno()].get(False)
                    print (chat)
                    conn2.send(chat)
                except Queue.Empty:
                    chat = "none"
                    time.sleep(2)




lock = threading.Lock()
global command
command = ""

sendqueues = {}
activeUsers = []
userfdmap = []

PORT2 = 8000
BUFFER = 1024

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
tcpsock.bind((HOST, PORT))

tcpsock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
tcpsock2.bind((HOST, PORT2))

threads=[]

while True:
    tcpsock.listen(10)
    print ("Server waiting\n")
    (conn, (ip,port)) = tcpsock.accept()
    q = Queue.Queue()
    lock.acquire()

    sendqueues[conn.fileno()] = q
    lock.release()

    print ("new thread with ", conn.fileno())
    newthread= ClientThread(conn, HOST, PORT)
    newthread.daemon = True
    newthread.start()
    newthread2 = ClientThreadRead(conn)
    newthread2.start()
    threads.append(newthread)
    threads.append(newthread2)


for t in threads:
    t.join()

print ("exited")

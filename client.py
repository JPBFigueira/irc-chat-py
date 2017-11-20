import socket
import sys
import collections
import time
import Queue
import threading
from threading import Thread
from SocketServer import ThreadingMixIn
HOST = 'localhost'
PORT = 9000
PORT2 = 8000
BUFFER = 1024

class ServerThread(Thread):
    def __init(self, socket):
        Thread.__init__(self)
        self.socket = SocketServer

    def run(self):
        rcv = self.socket.recv(BUFFER)
        print rcv
        user_name = raw_input("Enter username: ")
        self.socket.send(user_name)
        while True:
            command = raw_input("<command> ex. <send> <destination> <msg> ")
            self.socket.send(command)


class ServerThreadread(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket

    def run(self):
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.connect((HOST,PORT2))
        welcomemsg = s2.recv(BUFFER)
        print welcomemsg
        while True:
            chat = s2.recv(BUFFER)
            print chat
            time.sleep(5)

threads = []
global log
log = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
newthread = threading.Thread(target=ServerThread, args=(s,))
newthread.daemon = True
newthread.start()
newthread2 = threading.Thread(target=ServerThreadread, args=(s,))
#newthread2.daemon = True
newthread2.start()
threads.append(newthread)
threads.append(newthread2)
while True:
    for t in threads:
        t.join(600)
        if not t.isAlive():
            break
    break

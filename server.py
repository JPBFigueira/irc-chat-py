import socket
import select
import sys
import Queue

HOST = 'localhost'
PORT = 9000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('ServerSocket created\n')
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
inputs = [serverSocket]
outputs = []
messages= {}
try:
    serverSocket.bind((HOST,PORT))
except socket.error as msg:
    print('failed binding\n')
    sys.exit()
print('binded\n')

#Start listening

serverSocket.listen(10)
print('ready to listen\n')

inputs.append(serverSocket)

while(1):
    readable, writeable, exceptional = select.select(inputs,outputs,inputs)
    for sock in readable:#new connection received
        if sock == serverSocket:
            connection, client_addr = sock.accept()
            inputs.append(connection)
            messages[connection] = Queue.Queue()
        else: #not a new connection
            string = sock.recv(1024)
            if string: #something in the socket
                messages[sock].put(string)
                if sock not in outputs:
                    outputs.append(sock)
            else:#no data, socket is broken
                if sock in outputs:
                    outputs.remove(sock)
                inputs.remove(sock)
                sock.close()
                del messages[sock]

    for sock in writeable:
        try:
            nxt_msg = messages[sock].get_nowait()
        except Queue.Empty:
            outputs.remove(sock)

        else:
            nxt_msg = nxt_msg + 'Fully Connected\n'
            sock.send(nxt_msg)



#metodo broadcast para todos os clientes
#def broadcast(server_socket, sock, message):
#    for socket in socket_list:
#        if socket!= serverSocket and socket != sock:
#            try:
#                socket.send(message)
#            except:
#                #broken conn
#                socket.close()
#                #broken socketfd
#                if socket in socket_list:
#                    socket_list.remove(socket)

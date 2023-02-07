import socket
import _thread as thread

from client import *

MAX_DATA = 4500
DEFAULT_PORT = 80


def newServerSocket():

    try:
        print("Starting")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = '127.0.0.1'
        port = 8000

        s.bind((host, port))
        s.listen()

        while True:
            client, addr = s.accept()
            print("* new connection from %s" % str(addr))
            thread.start_new_thread(client_thread, (client, addr))

    except (socket.error):
        if s:
            s.close()
        print('Starting error')



def client_thread(client, Clientaddress):
    header = client.recv(MAX_DATA)

    headerLines = header.split(b"\n")

    #split the request (URI)
    request = headerLines[0].split(b" ")[1]

    #find the serverAddress (port set as default)
    for line in headerLines:
        if line.find(b"Host:") >= 0:
            host = line.split(b":")[1].strip()

    print("Host %s" % str(host), "  --  Request %s" % str(request))
    newClientSocket(request, (host, DEFAULT_PORT))





if __name__ == '__main__':
    print("execute")
    newServerSocket()

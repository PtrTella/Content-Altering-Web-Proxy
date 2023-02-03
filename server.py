import socket
import _thread as thread

from client import *

MAX_DATA = 4500


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



def client_thread(client, address):
    request = client.recv(MAX_DATA)

    #split the request
    addr_start = request.find('://')
    addr_end = request.find()

    newClientSocket(request, addr)





if __name__ == '__main__':
    print("execute")
    newServerSocket()

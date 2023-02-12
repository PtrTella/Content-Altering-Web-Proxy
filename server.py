import socket
import _thread as thread

from client import *
from content_altering import *

MAX_DATA = 4500

def newServerSocket():

    try:
        print("Starting")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = '127.0.0.1'
        port = 8000

        s.bind((host, port))
        s.listen()
        #print(socket.gethostname())

        while True:
            client, addr = s.accept()
            print("--> New connection from %s" % str(addr))
            thread.start_new_thread(client_thread, (client,))


    except (socket.error):
        if s:
            print('Starting error')
            s.close()
    
    except KeyboardInterrupt:
        print("CLOSE CONNECTION")
        s.close


def client_thread(client):
    header = client.recv(MAX_DATA)    

    response = newClientSocket(header)

    status(response)
    response = text_modification(response)
    
    client.sendall(response)
    client.close()

if __name__ == '__main__':
    print("execute")
    newServerSocket()

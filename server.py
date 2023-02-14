import socket
import _thread as thread

from client import *
from content_altering import *


def newServerSocket():
#function for the server side of the proxy
    try:
        print("Starting")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #configuration of the proxy
        host = '127.0.0.1'
        port = 8000

        s.bind((host, port))
        s.listen()

        #loop to get and create a socket for all the connexions on the proxy
        while True:
            client, addr = s.accept()
            print("--> New connection from %s" % str(addr))
            thread.start_new_thread(client_thread, (client,))


    except (socket.error):
        if s:
            print('Starting error')
            s.close()
    #if we want to manually close the proxy
    except KeyboardInterrupt:
        print("CLOSE CONNECTION")
        s.close


def client_thread(client):
#function that manage
    header = client.recv(MAX_DATA)    

    response = newClientSocket(header) # we send the header of the HTTP request
    # we get the answer status code and we do the content altering thanks to ours functions
    status(response)
    response = text_modification(response)

    #we send back to our browser the modified anwser from the server
    client.sendall(response)
    client.close()

if __name__ == '__main__':
    print("execute")
    newServerSocket()

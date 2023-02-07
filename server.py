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
            print("--> New connection from %s" % str(addr))
            thread.start_new_thread(client_thread, (client,))

    except (socket.error):
        if s:
            s.close()
        print('Starting error')



def client_thread(client):
    header = client.recv(MAX_DATA)

    #split the request (URI)
    #request = headerLines[0].split(b" ")[1]
    #request = request.replace(b"http://", b"")

    

    #print("Host %s" % str(host))
    response = newClientSocket(header)

    # It's better to split again the response

    client.send(response)
    client.close()





if __name__ == '__main__':
    print("execute")
    newServerSocket()

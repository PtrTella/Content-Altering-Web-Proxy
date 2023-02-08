import socket
from contenent_altering import *

MAX_DATA = 4500
DEFAULT_PORT = 80


def newClientSocket(request:bytes):

    #find the serverAddress (port set as default)
    headerLines = request.split(b"\n")
    host = headerLines[1].split(b":")[1].strip()

    if host is None:
        return (b"Server Not found")
    else:
        serverAddress = (host, DEFAULT_PORT)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(serverAddress)
        s.send(request)
        #print(" |__ server address %s" % str(serverAddress))

        response = b""
        while True:
            # recive data from WebServer
            data = s.recv(MAX_DATA)  # check basic error on data?
            if not data:
                break
            response += data
        
        s.close()
        return response

    except (socket.error):
        if s:
            s.close()

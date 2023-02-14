import socket
from content_altering import *


MAX_DATA = 4500 #maximum size of the data that can be receive from the server
DEFAULT_PORT = 80 #default port for HTTP


def newClientSocket(request:bytes):
#function for the client  side of the proxy

    #find the serverAddress (port set as default)
    headerLines = request.split(b"\n")
    host = headerLines[1].split(b":")[1].strip()

    if host is None:
        return (b"Server Not found")
    else:
        serverAddress = (host, DEFAULT_PORT)

    try:
        #socket that connect to the server, send the request and receive the answer
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(serverAddress)
        s.send(request)


        response = b""
        while True:
            # receive data from WebServer
            data = s.recv(MAX_DATA)
            if not data: # we close the connection where there is no more data
                break
            response += data # to manage the case where the data is receive in multiple segments
        
        s.close()
        return response # we return the total answer from the server

    except (socket.error):
        if s:
            s.close()

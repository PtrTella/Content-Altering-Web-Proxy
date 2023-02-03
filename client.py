import socket
MAX_DATA = 4500

def newClientSocket(request, addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.send(request)

        while True:
            #recive data from WebServer
            data = s.recv(MAX_DATA) #check basic error on data?
    
    except(socket.error):
        if s:
            s.close()

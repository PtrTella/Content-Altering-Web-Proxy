import socket,sys
import _thread as thread

 # how many pending connections queue will hold
MAX_DATA_RECV = 4096  # max number of bytes we receive at once
counter = 0 #to count the number of active connexion
host="127.0.0.1"
port =8080

def main():

    print("Proxy Server Running")
    print('Your browser should be configured with the host= ', host)
    print('and the port', port)

    try:
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # associate the socket to host and port
        s.bind((host, port))

        # listenning
        s.listen()


    except (socket.error):

        if s:
            s.close()

        print("Could not open socket:")

        sys.exit(1)

    while 1:
        print("the server is ready,  we are waiting for connexion ...")
        conn, client_addr = s.accept()
        # renvoie un objet socket (conn) pour communiquer avec ,et renvoie l'address du client sous forme de tuple (('host',port))


        # create a thread to handle request
        thread.start_new_thread(proxy_thread, (conn, client_addr))

    s.close()



def proxy_thread(conn, client_addr):
    # get the request from browser
    request = conn.recv(MAX_DATA_RECV)



    # parse the first line
    first_line = request.split(b'\n')[0]

    # get url
    url = first_line.split(b' ')[1]

    print("Request", first_line, client_addr)
    # print "URL:",url
    # print

    # find the webserver and port
    http_pos = url.find(b'://')  # find pos of ://
    if (http_pos == -1):
        temp = url
    else:
        temp = url[(http_pos + 3):]  # get the rest of url

    port_pos = temp.find(b':')  # find the port pos (if any)

# find end of web server
    webserver_pos = temp.find(b'/')
    if webserver_pos == -1:
        webserver_pos = len(temp)

    webserver = ""
    port = -1
    if (port_pos == -1 or webserver_pos < port_pos):  # default port
        port = 80
        webserver = temp[:webserver_pos]
    else:  # specific port
        port = int((temp[(port_pos + 1):])[:webserver_pos - port_pos - 1])
        webserver = temp[:port_pos]

    try:
        # create a socket to connect to the web server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, port))
        s.send(request)  # send request to webserver

        while 1:
            # receive data from web server
            data = s.recv(MAX_DATA_RECV)

            if (len(data) > 0):
                # send to browser
                conn.send(data)
            else:
                break
        s.close()
        conn.close()
    except (socket.error):
        if s:
            s.close()
        if conn:
            conn.close()
        print("Peer Reset", first_line, client_addr)
        sys.exit(1)


main()
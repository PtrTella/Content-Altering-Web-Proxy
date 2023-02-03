import socket,sys
import _thread as thread

 # how many pending connections queue will hold
MAX_DATA_RECV = 4500  # max number of bytes we receive at once
counter = 0 #to count the number of active connexion
host="127.0.0.1"
port =8080

def main():

    print("Proxy Server Running")
    print('Your browser should be configured with the host: ', host)
    print('and the port', port)

    try:
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # associate the socket to host and port
        s.bind((host, port))

        # listening
        s.listen()


    except (socket.error):

        if s:
            s.close()

        print("Could not open socket:")

        sys.exit(1)

    while 1:
        conn, client_addr = s.accept()
        # renvoie un objet socket (conn) pour communiquer avec ,et renvoie l'address du client sous forme de tuple (('host',port))


        # create a thread to handle request
        thread.start_new_thread(proxy_thread, (conn, client_addr))

    s.close()



def proxy_thread(conn, client_addr):
    # get the request from browser
    request = conn.recv(MAX_DATA_RECV)



    # parse the first line

    print(request)
    first_line = request.split(b'\n')[0]
    print(type(first_line))
    print(first_line)

    # get url
    url = first_line.split(b' ')[1]
    print(url)
    print("Request: ", first_line, client_addr)


    # find the webserver and port
    http_pos = url.find(b'://')  # find pos of ://

    if (http_pos == -1):
        temp = url
    else:
        temp = url[(http_pos + 3):]  # get the rest of url

    port_pos = temp.find(b':')  # find the port pos (if any)
    print(temp) #URL without the http://
# find end of web server
    webserver_pos = temp.find(b'/')
    if webserver_pos == -1:
        webserver_pos = len(temp)



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
        print('address of the web server:', webserver,' coresponding port: ',port)
        s.send(request)  # send request to webserver
        response =b""
        while 1:
            # receive data from web server
            data = s.recv(MAX_DATA_RECV)
            print(len(data))
            if not data:
                break
            response += data
            status(response)
            print(len(response))
            response_lines = response.split(b"\r\n")
            content = b"\r\n".join(response_lines[4:])
            print (content)
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
def status(arg:bytes):
    first_header = arg.split(b'\r')[0]
    status = first_header.split(b' ')
    print(status)
    status_code = status[1]
    print(len(status))
    if len(status) > 3:
        status_phrase = status[2] + (b' ') + status[3]
    else:
        status_phrase = status[2]
    # We put them in type string to be concatenate more easily
    status_code_str = status_code.decode(encoding="UTF-8")
    status_phrase_str = status_phrase.decode(encoding="UTF-8")
    print("The answer of the HTTP request is: ")
    print(status_code_str, status_phrase_str)

def Stockholm(arg:bytes):
    if b'Stockholme' in arg:
        print("Stockholm trouvé")

main()
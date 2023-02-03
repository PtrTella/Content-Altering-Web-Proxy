import socket
import _thread as thread


def main():

    def run():
        print("Starting")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = '127.0.0.1'
        port = 8000

        s.bind((host, port))
        s.listen()

        while True:
            client, addr = s.accept()
            print("* new connection from %s" % str(addr))
            client.close
    run()


if __name__ == '__main__':
    print("execute")
    main()

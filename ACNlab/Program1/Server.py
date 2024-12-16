import socket
import os

def startServer(host = "127.0.0.1",port = 6060):
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.bind((host,port))
    serverSocket.listen(1)
    print(f"SERVER IS LISTENING ON HOST {host}:{port} ")

    while(True):
        conn, addr = serverSocket.accept()
        print(f"connection from {addr}")

        try:
            filename = conn.recv(1024).decode()
            print(f"Requested filename : {filename}")

            if(os.path.isfile(filename)):
                with open(filename,'r') as file :
                    content = file.read()
                    conn.sendall(content.encode())

            else :
                conn.sendall(b"File not found\n")
        finally:
            conn.close()

if(__name__ == "__main__"):
    startServer()

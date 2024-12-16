import socket

def requestSocket(host = "127.0.0.1", port = 6060):
    clientServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        clientServer.connect((host,port))
        print(f"Connected to port {port}, host {host}")

        filename = input("\n Enter the filename to request : ")
        if(filename.lower() == "exit"):
            print("\n Exit statement called")
            return
        
        clientServer.sendall(filename.encode())

        response = b""
        while True:
            data = clientServer.recv(1024)
            if not data:
                break
            response += data

        print("response from server : ")
        print(response.decode())

    finally:
        clientServer.close()

if(__name__ == "__main__"):
    requestSocket()

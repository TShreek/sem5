import socket

def udpServer(host = "127.0.0.1", port =6060):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((host,port))
    print(f"Server is running at {host}:{port}")

    while(True):
        mess, addr = serverSocket.recvfrom(1024)
        message = mess.decode()
        length = len(message)
        upperCaseMessege = message.upper()

        response = f"{upperCaseMessege}|{length}"
        serverSocket.sendto(response.encode(),addr)

if(__name__ == "__main__"):
    udpServer()

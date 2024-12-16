import socket

def udpClient(host = "127.0.0.1", port = 6060):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Type exit to exit ")

    while(True):
        messege = input("Enter an input to send: ")
        if(messege.lower() == "exit"):
            break
        clientSocket.sendto(messege.encode(),(host,port))

        response, _ = clientSocket.recvfrom(1024)
        uppercase,char_count = response.decode().split("|")
        print(f"Server says: {uppercase}, Charecters : {char_count}")
        
    clientSocket.close()

if(__name__ == "__main__"):
    udpClient()

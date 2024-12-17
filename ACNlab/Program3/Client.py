import socket

def calculate_crc(data, generator):
    """Perform CRC division and return the checksum."""
    padded_data = data + '0' * (len(generator) - 1)
    data_len, gen_len = len(padded_data), len(generator)

    padded_data = list(padded_data)
    generator = list(generator)

    for i in range(data_len - gen_len + 1):
        if padded_data[i] == '1':  # Perform XOR only when leading bit is 1
            for j in range(gen_len):
                padded_data[i + j] = str(int(padded_data[i + j]) ^ int(generator[j]))

    return ''.join(padded_data[-(gen_len - 1):])

def start_client(host='localhost', port=6000):
    while True:
        message = input("Enter message (binary) or type 'exit' to quit: ")
        if message.lower() == 'exit':
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
                client_socket.sendto("exit,exit".encode(), (host, port))
            print("Exiting client.")
            break

        generator = input("Enter generator (binary): ")
        checksum = calculate_crc(message, generator)
        print(f"Checksum code: {checksum}")

        # Send data with checksum to the server
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            client_socket.sendto(f"{message},{checksum}".encode(), (host, port))

if __name__ == "__main__":
    start_client()

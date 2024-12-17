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

def start_server(host='localhost', port=6000):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server listening on {host}:{port}...")

        while True:
            data, addr = server_socket.recvfrom(1024)
            received_data = data.decode()

            # Check for client exit
            if 'exit' in received_data:
                print("Client has exited. Shutting down the server.")
                break

            received_message, received_checksum = received_data.split(',')
            generator = input("Enter generator (binary): ")

            # Compute CRC and validate
            computed_checksum = calculate_crc(received_message + received_checksum, generator)
            print(f"Received message (CRC): {received_message + received_checksum}")
            print(f"Received checksum: {received_checksum}")

            if all(bit == '0' for bit in computed_checksum):
                print(f"Data from {addr} is valid.")
            else:
                print(f"Data from {addr} is invalid.")

if __name__ == "__main__":
    start_server()

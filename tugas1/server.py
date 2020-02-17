import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 3000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print('connection from', client_address)

    # Receive file
    with open('file_received' + '.jpg', 'a+b') as file:
        while True:
            isi = connection.recv(1024)
            if not isi:
                file.close()
                break
            file.write(isi)

    # Clean up the connection
    connection.close()
sock.close()


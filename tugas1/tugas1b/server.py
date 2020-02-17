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

    # Receive filename
    filename = connection.recv(1024)
    file = open(filename.decode(), 'rb')
    isi = file.read() #1024
    while isi:
        connection.sendall(isi)
        isi = file.read()
    file.close()
    # Clean up the connection
    connection.close()
sock.close()


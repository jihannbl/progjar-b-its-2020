import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.12', 3000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # Send data
    namafile = input('Masukkan nama file : ')
    file = open(namafile, 'rb')
    isi = file.read()
    print('sending file')
    sock.sendall(isi)
finally:
    print('closing socket')
    sock.close()

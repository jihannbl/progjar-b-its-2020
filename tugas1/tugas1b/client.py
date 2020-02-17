import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 3000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # Send data
    namafile = input('Masukkan nama file (request): ')
    sock.sendall(namafile.encode())

    with open('hasil_'+ namafile, 'a+b') as file:
        while True:
            isi = sock.recv(1024)
            if not isi:
                file.close()
                break
            file.write(isi)
finally:
    print('closing socket')
    sock.close()

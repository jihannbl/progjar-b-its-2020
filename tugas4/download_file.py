import socket
import sys
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8000
server_address = ('127.0.0.1', port)
print("Connecting to Server: 127.0.0.1", " Port:", port)
sock.connect(server_address)

try:
    filename = input('Masukkan nama file : ')
    cm = "download_file " + filename
    print("Requesting File to Server")
    sock.send(cm.encode())

    data = sock.recv(4096)
    f = open(filename, "wb")
    f.write(data)
    f.close()

    print("File has been Downloaded")
finally:
    print("Closing Connection")
    sock.close()
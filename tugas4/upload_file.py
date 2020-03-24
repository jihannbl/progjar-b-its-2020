import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8000
server_address = ('127.0.0.1', port)
print("Connecting to Server: 127.0.0.1" , " Port:", port)
sock.connect(server_address)

try:
    filename=input('Masukkan nama file : ')
    f = open(filename,"rb")
    file = f.read(2048)
    f.close()
    file = file.decode()
    cm = "upload_file "+filename+" "+file
    print ("Uploading File")
    sock.send(cm.encode())

    data = sock.recv(2048).decode()
    print(data)
finally:
    print("Closing Connection")
    sock.close()
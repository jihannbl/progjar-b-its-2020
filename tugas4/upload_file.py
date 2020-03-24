import socket
import sys
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8000
server_address = ('127.0.0.1', port)
print("Connecting to Server: 127.0.0.1" , " Port:", port)
sock.connect(server_address)
command = "upload_file"
try:
    filename=input('Masukkan nama file : ')
    f = open(filename,"rb")
    # # file = f.read(2048)
    # file = base64.b64encode(f.read())
    # f.close()
    # # file = file.decode()
    # # cm = "upload_file "+filename+" "+file
    # cm = "upload_file ".encode() + filename.encode() + (b" ") + file
    # print ("Uploading File")
    # sock.send(cm)
    #
    # data = sock.recv(2048).decode()
    # print(data)
    content = base64.b64encode(f.read())
    f.close()
    f = open("temp", "wb")
    f.write(content)
    f.close()
    f = open("temp", "rb")
    request = command.encode() + filename.encode() + (b" ") + f.read(1024)
    print(request)
    while (request):
        sock.send(request)
        request = f.read(1024)
        response = sock.recv(1024)
    f.close()
    os.remove("temp")
    print(response)
finally:
    print("Closing Connection")
    sock.close()
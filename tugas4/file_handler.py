import shelve
import uuid
import socket
import os
import base64

class File_Handle:
    def __init__(self):
        if not os.path.exists("files"):
            os.makedirs("files")
    def upload(self,filename=None,file=None):
        
        f = open("files/"+filename,"wb")
        f.write(file)
        return True

    def download(self,filename=None):
        f = open("files/" +filename, "rb")
        res = f.read()
        f.close()
        res = str(res, "utf-8")
        return res

    def list(self):
        list_file = os.listdir("files")
        return list_file

if __name__=='__main__':
    p = File_Handle()
    print(p.list())



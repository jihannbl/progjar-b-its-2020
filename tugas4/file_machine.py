from file_handler import File_Handle
import json
import logging

'''
        PROTOCOL FORMAT

string terbagi menjadi 2 bagian yang dipisahkan oleh spasi
Format : command *spasi* parameter *spasi* parameter

        FITUR

a. Meletakkan File
   Untuk meletakkan file ke dalam folder "storage"
   Request : add_file
   Parameter : namafile *spasi* isi dari file
   Response : berhasil -> "File Added"
              gagal -> "ERROR"

b. List File
   Untuk melihat list file di dalam folder 'storage'
   Request : list_file
   Parameter: -
   Response: list file yang ada dalam folder 'storage'

c. Mengambil File
   Untuk mengambil file berdasarkan nama file dari folder 'storage'
   Request : get_file
   Parameter : namafile yang ingin diambil
   Response: file ter download pada folder tempat script berada

d. Jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = File_Handle()

class Machine:
    def proses(self,s):
        str = s.split(" ")
        try:
            cmd = str[0].strip()
            if (cmd=='upload_file'):
                filename = str[1].strip()
                file = str[2].strip()
                print("upload_file")
                print("Uploading",filename)
                p.upload(filename,file.encode())
                return "File Uploaded"

            elif (cmd=='download_file'):
                filename = str[1].strip()
                print("download_file")
                print("Downloading", filename)
                res = p.download(filename)
                return res

            elif (cmd=='list_file'):
                logging.info("list_file")
                data = {}
                data['files'] = []
                res = p.list()
                for filename in res:
                    data['files'].append({"filename":filename})
                return json.dumps(data, indent=4)
            else:
                return "Command Error"
        except:
            return "Failed"


if __name__=='__main__':
    machine = Machine()
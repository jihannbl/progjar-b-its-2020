from file_handler import File_Handle
import json
import logging

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

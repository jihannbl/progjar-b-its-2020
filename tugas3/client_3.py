import logging
import requests
import os
import threading

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpeg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}") # thread {i}
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

inilist = ['https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg',
        'https://1ryzas42x65e2oosia40bgli-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/WBB-site-image-838x400.jpg',
        'https://cdn.idntimes.com/content-images/post/20170831/aaeaaqaaaaaaaanmaaaajgvjogm4njjjltqwntqtngyxoc05odu1ltq3zmvhmwvhyjg5mq-2af18cd5c3afc9654dae30303bb7ab63.jpg']
threads = []
for x in inilist:
    t = threading.Thread(target=download_gambar,args=(x,))
    threads.append(t)

for trd in threads:
    trd.start()

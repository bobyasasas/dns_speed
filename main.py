import time
import requests
import os

file_url = 'https://down.heleguo.top/download/100MB.zip'
file_path = './download'
file_name = '/kai.test'
ip = '104,20,18,206'
if not os.path.exists(file_path):
    os.mkdir(file_path)
r = requests.get("http://104.20.18.206/download/100MB.zip", headers={'Host': 'down.heleguo.top'},
                 stream=True)
f = open(file_path + file_name, "wb")
file_size = int(r.headers['content-length'])
download_size = 0
download_percent = 0
start_time = time.time()
second_start_time = time.time()
temp_size = 0
for chunk in r.iter_content(chunk_size=1024):
    if chunk:
        f.write(chunk)
        download_size += len(chunk)
        download_percent = (download_size / file_size) * 100
        if time.time() - start_time > 1:
            start_time = time.time()
            speed = download_size - temp_size
            print(download_percent, '%', speed / (1024 ** 2), 'MB/s')
            temp_size = download_size
end_time = time.time()
print("平均速度为:", (file_size / (end_time - second_start_time)) / 1024 ** 2, 'MB/s')
f.close()
os.remove(file_path + file_name)

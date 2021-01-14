# /usr/bin/env python2
# -*- coding:utf-8 -*-
# auther: d3ckx1
# time: 2021/01/12
# 需要安装 PhantomJS，下载地址：https://phantomjs.org/download.html
# Linux/macOS命令：export PATH=/Users/d3ckx1/phantomjs-2.1.1-macosx/bin:$PATH
# Windows添加环境变量

import requests
import sys
import time
from selenium import webdriver

banner = """
                                        
   ____ _               _    _   _      _  ___                   
  / ___| |__   ___  ___| | _| | | |_ __| |/ _ \ _ __   ___ _ __  
 | |   | '_ \ / _ \/ __| |/ / | | | '__| | | | | '_ \ / _ \ '_ \ 
 | |___| | | |  __/ (__|   <| |_| | |  | | |_| | |_) |  __/ | | |
  \____|_| |_|\___|\___|_|\_\\___/|_|  |_|\___/| .__/ \___|_| |_|
                                               |_|               
   
			 C0de by d3ckx1   2021-01-12

"""
print banner


def go_get():
    heads = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    try:
        requests.packages.urllib3.disable_warnings() #解决InsecureRequestWarning警告
        req = requests.get(url, headers=heads, timeout=5, verify=False,)

        if req.status_code == 200:
            print ("[+] " + url + " URL is open!")
            f = open('ok.txt', 'a')
            f.write(url)
            f.write("\n")
            png_name = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            print "[+] 开始截图,请稍等...."
            brower = webdriver.PhantomJS()
            brower.get(url)
            brower.maximize_window()
            brower.save_screenshot('%s.png'% png_name)
            brower.close()
            print "[+] 截图成功!!!"
            time.sleep(2)


        elif req.status_code == 301 or req.status_code == 302:
            print ("[!] " + url + " URL is jump!")
            f = open('jump.txt', 'a')
            f.write(url)
            f.write("\n")

        else:
            print ("[-] " + url + " URL is not found!")

    except:
        print("[-] " + url + " URL请求超时/失败!")
        f = open('not_found.txt','a')
        f.write(url)
        f.write('\n')


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] == '-h':
        print('Usage :python checkurlopen.py ip.txt')

    else:
        localtime = time.asctime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()) )
        print "本次扫描时间为：", localtime
        print '-----------------------------------------------------------'
        file = open(sys.argv[1])
        for urls in file.readlines():
            url = urls.strip()
            go_get()
        print '-----------------------------------------------------------'
        print "URL is Check over!"






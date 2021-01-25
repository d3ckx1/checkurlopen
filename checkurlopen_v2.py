# /usr/bin/env python2
# -*- coding:utf-8 -*-
# auther: d3ckx1
# time: 2021/01/12
# 需要安装 PhantomJS，下载地址：https://phantomjs.org/download.html
# Linux/macOS命令：export PATH=/Users/d3ckx1/phantomjs-2.1.1-macosx/bin:$PATH
# Windows添加环境变量

import socket
import sys
import time
from selenium import webdriver
import threading
from IPy import IP

banner = """
                                        
   ____ _               _    _   _      _  ___                   
  / ___| |__   ___  ___| | _| | | |_ __| |/ _ \ _ __   ___ _ __  
 | |   | '_ \ / _ \/ __| |/ / | | | '__| | | | | '_ \ / _ \ '_ \ 
 | |___| | | |  __/ (__|   <| |_| | |  | | |_| | |_) |  __/ | | |
  \____|_| |_|\___|\___|_|\_\\___/|_|  |_|\___/| .__/ \___|_| |_|   
                                               |_|               
                  
                          v2.0   C0de by d3ckx1

"""
print banner

WEB_PORTS_LIST = [    80,    81,    82,    83,    84,    85,    86,    87,    88,    89,\
                      90,   443,  4848,  7001,  7002,  7778,  8000,  8001,  8002,  8003,\
                    8004,  8005,  8006,  8007,  8008,  8009,  8010,  8020,  8030,  8040,\
                    8043,  8050,  8060,  8066,  8069,  8070,  8080,  8081,  8082,  8083,\
                    8084,  8085,  8086,  8087,  8088,  8089,  8090,  8096,  8099,  8100,\
                    8200,  8443,  8480,  8488,  8588,  8688,  8788,  8800,  8888,  8900,\
                    9000,  9001,  9002,  9003,  9004,  9005,  9006,  9007,  9008,  9909,\
                    9010,  9020,  9030,  9040,  9043,  9050,  9060,  9070,  9080,  9081,\
                    9082,  9083,  9084,  9085,  9086,  9087,  9088,  9089,  9090,  9100,\
                    9200,  9300,  9400,  9500,  9600,  9700,  9800,  9900,  9999,  8500,\
                    8983,  3000,  5601,  8181,  888,  10000, 10443,]


def tcpopen(host):
    for i in WEB_PORTS_LIST:
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(1)
            tcpscan = (str(host),i)
            sock.connect(tcpscan)
            print "[+] IP: " + str(host) + " TCP: " + str(i) + " is open!"
            if str(i) == "80":
                tcpok1 = open('tcpok.txt', 'a+')
                tcpok1.write("http://"+str(host)+"/")
                tcpok1.write('\r\n')
                tcpok1.close()

            elif str(i) == "443":

                tcpok2 = open('tcpok.txt', 'a+')
                tcpok2.write("https://"+str(host)+"/")
                tcpok2.write('\r\n')
                tcpok2.close()

            elif str(i) == '8443':

                tcpok2 = open('tcpok.txt', 'a+')
                tcpok2.write("https://" + str(host) +":"+str(i)+ "/")
                tcpok2.write('\r\n')
                tcpok2.close()
            else:
                tcpok3 = open('tcpok.txt', 'a+')
                tcpok3.write("http://"+str(host)+":"+str(i)+"/")
                tcpok3.write('\r\n')
                tcpok3.close()

        except:
            pass



def screen():
    try:
        urls = open('tcpok.txt', 'rb')
        for urlss in urls.readlines():
            url = urlss.strip()
            print url
            jpg_name = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            print "[+] To start taking a Web Screenshot, please wait...."
            brower = webdriver.PhantomJS()
            brower.set_page_load_timeout(5)
            brower.set_script_timeout(5)
            try:
                brower.get(url)
                brower.maximize_window()
                brower.save_screenshot('%s.jpg' % jpg_name)
                print "---- URL Name: "+ brower.title+ "----"
                brower.close()
                print "[+] Screenshot successful!!"
                time.sleep(1)

            except:
                pass

    except:
        pass


if __name__ == '__main__':

    if len(sys.argv) == 1 or sys.argv[1] == '-h':
        print('Usage :python checkurlopen.py ip.txt')

    else:
        localtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        print "The scanning time is: ", localtime
        print '-----------------------------------------------------------'
        ip = IP(sys.argv[1])
        for host in ip:
            t1 = threading.Thread(target=tcpopen(host),args=(100,110))
            t1.setDaemon(True)
            t1.start()
        print "url is write it, please check 'tcpok.txt'"

        t2 = threading.Thread(target=screen(),args=(10,12))
        t2.setDaemon(True)
        t2.start()
        print '-----------------------------------------------------------'
        print "URL is Check over!"

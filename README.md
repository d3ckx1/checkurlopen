# checkurlopen
使用范围：
在安全服务中用于批量检查URL资产开放情况，并且拍摄网站快照.... 第一版（checkurlopen_v1.0）

在内网渗透（红队攻击）中，可以对整个C段/B段/单IP，进行自动化探测与拍摄WEB快照，解放双手...(我默认写了常用/不常用的187个端口) 第二版（checkurlopen_v2）


第一版（checkurlopen_v1.0）

使用方法：python checkurlopen.py ip.txt

演示图：
![Image text](https://github.com/d3ckx1/checkurlopen/blob/main/截屏2021-01-14%20下午4.59.30.png)
![Image text](https://github.com/d3ckx1/checkurlopen/blob/main/截屏2021-01-14%20下午4.59.52.png)


第二版（checkurlopen_v2）

使用方法：python checkurlopen.py 172.16.24.229
或 172.16.24.0/24 
或 172.16.0.0/16

![Image text](https://github.com/d3ckx1/checkurlopen/blob/main/截屏2021-01-25%20下午5.11.02.png)


依赖插件：PhantomJS
下载地址：https://phantomjs.org/download.html （下载自己对应操作系统版本）

Linux/macOS 命令：export PATH=/Users/d3ckx1/phantomjs-2.1.1-macosx/bin:$PATH

Windows 需要把PhantomJS添加环境变量

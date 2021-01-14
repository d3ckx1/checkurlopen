# checkurlopen

介绍：用于批量判断目标URL是否能访问，如果http访问成功，保存成“ok.txt”，并且自动进行截图保存，如果http访问不成功，保存成“not_found.txt”，方便后期你验证。

使用范围：安全服务中批量检查URL资产，内网渗透中，对探测到的http批量资产，进行自动化可用性访问并截图保存，解放双手。

后期还会继续追加新功能！！！！

使用方法：python checkurlopen.py ip.txt

演示图：
![Image text](https://github.com/d3ckx1/checkurlopen/blob/main/截屏2021-01-14%20下午4.59.30.png)
![Image text](https://github.com/d3ckx1/checkurlopen/blob/main/截屏2021-01-14%20下午4.59.52.png)


依赖插件：PhantomJS
下载地址：https://phantomjs.org/download.html （下载自己对应操作系统版本）

Linux/macOS 命令：export PATH=/Users/d3ckx1/phantomjs-2.1.1-macosx/bin:$PATH

Windows 添加环境变量

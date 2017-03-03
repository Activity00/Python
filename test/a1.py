#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年2月20日
爬取当当网
@author: 武明辉
'''
import chardet
import urllib
data=urllib.urlopen('http://www.dangdang.com').read()
print chardet.detect(data)
print data.decode('gbk')#设置编码
print data.encode('urf-8','ignore')

#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年2月20日
爬取csdn
@author: 武明辉
'''
from _csv import Error
import sys
import traceback
import urllib

from pip._vendor.requests.exceptions import HTTPError


try:
    urllib.urlopen('http://blog.csdn.net')
except Exception as e:
    print '宜昌概要：'
    print e
    print '------------'
    error_info=sys.exc_info()
    print '异常类型：'+str(error_info[0])
    print("异常信息或参数："+str(error_info[1]))
    print("调用栈信息的对象："+str(error_info[2]))
    print("已从堆栈中“辗转开解”的函数有关的信息："+str(traceback.print_exc()))
#（2）捕获URLError
try:
    urllib.urlopen("http://blog.csdn.net")
except Error as er2: 
    if hasattr(er2,"code"):
        print("URLError异常代码：")
        print(er2.code)
    if hasattr(er2,"reason"):
        print("URLError异常原因：")
        print(er2.reason)
#--------------------------------------------------
#（3）捕获HTTPError
try:
    urllib.urlopen("http://blog.csdn.net")        
except  HTTPError as er3: 
    print("HTTPError异常概要：")
    print(er3)
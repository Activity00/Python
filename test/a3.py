#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年2月20日

@author: 武明辉
'''
import urllib
import urllib2
import cookielib

def postData():
    '''1.post方式登录csdn'''
    values={}
    values['username']='1032662429@qq.com'
    values['password']='1032662429'
    values['lt']='LT-944589-MhhIt3aWpbMjfEOJrU1x5FmgU727eq'
    values['execution']='e3s1'
    values['_eventId']='submit'
    info=urllib.urlencode(values).encode('utf-8')
    url='http://passport.csdn.net/account/login'
    try:
        cj=cookielib.CookieJar()
        data=urllib.urlopen(url, info).read()
    except Exception as e:
        print e
    return data

def getData():
    '''2.get方式搜索简书'''
    keyword = "简书" #搜索关键词
    keyword = urllib.quote(keyword)#编码
    url = "http://www.baidu.com/s?wd="+keyword
    try:
        req = urllib2.Request(url)
        data = urllib2.Request.urlopen(req).read()
    except Exception as er: 
        print("异常概要：")
        print(er)
    return data   

print postData()
print getData()
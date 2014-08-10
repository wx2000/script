# -*- coding:utf-8 -*-
__author__ = 'apple'
__date__ = '2014-08-08 11:27'

#!/usr/bin/python

import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re

print '中文'

# login homepage中文
hosturl = 'https://www.f2pool.com/user/signup'

#post data
posturl = 'https://www.f2pool.com/user/signin'

# Set cookie, download cookie from server ,and then send to server with request
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

# open weblogin page, (download cookie then send cookie to server with post data
h = urllib2.urlopen(hosturl)

# stru header
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
           'Referer' : '******'}

# stru Post data
postData = {'op' : 'dmlogin',
            'f' : 'st',
            'user' : '******', # your username
            'pass' : '******', # your password (maybe encrpt)
            'rmbr' : 'true',   # data depend on web
            'tmp' : '0.7306424454308195'  # data depend on web

            }

# encode Post data
postData = urllib.urlencode(postData)

# urllib2 request to posturl with postdata and header
request = urllib2.Request(posturl, postData, headers)
print request
response = urllib2.urlopen(request)
text = response.read()
print text

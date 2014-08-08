__author__ = 'apple'

# https://www.f2pool.com/user/signup
#     action=https://www.f2pool.com/user/signin

#
# input 4 items
# name
# email
# password
# confirm_password

import httplib
import urllib
import urllib2
import cookielib

import requests

regname = 'pet23rt'
regemail = 'pet23rt@gmail.com'
regpassword = 'pet23rtf2'
url = "http://www.f2pool.com/user/signup"

values = [ ('name', regname),
           ('email', regemail),
           ('password', regpassword),
           ('confirm_password', regpassword) ]

print( urllib.urlencode(values))

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
# print(req)
response = urllib2.urlopen(req)
html = response.read()
# html = fd.decode('gb18030').encode('utf-8')

print(html)
__author__ = 'apple'

import urllib2

# create urllib instance
o = urllib2.build_opener()

# open a web site
f = o.open('http://itercast.com/ask')

# get web page
f.read()




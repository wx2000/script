__author__ = 'apple'
#coding:utf-8
import urllib
import time
import os

url = ['']*100
page = 1
link = 1
while page <= 2:
# read blog homepage. 
  con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1496915375_0_' + str(page) + '.html').read()
  i = 0
  title = con.find(r'<a title=')
  href = con.find(r'href=',title)
  html = con.find(r'.html',href)
 
# get articles url
  while title != -1 and href != -1 and html != -1 and i < 50:
    url[i] = con[href+6:html+5]
    print(link, url[i])

    title = con.find(r'<a title=',html)
    href = con.find(r'href=',title)
    html = con.find(r'.html',href)
    
# write articles to files    
    #content = urllib.urlopen(url[i]).read() # get blog article content
    filename = url[i][-26:]
    #open(r'wo/' + filename,'w+').write(content) # save to file
    print 'writing', filename
    time.sleep(1)
    i = i + 1
    link = link + 1
    
  else:
    print page ,'page find end'
    page = page + 1

else:
    print 'all finish'




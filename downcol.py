# coding = UTF-8
#!/usr/bin/env python

#@Author: wklken
#@Mail: wklken@yeah.net
#@Date: 20120807
#@version 0.1
#@desc: base function to download csdn column!


print "begin...."

import urllib2,socket
import re
import os,sys


# 该页最后一个中文链接，尾页

p2first = re.compile(ur'下一页</a> <a href="(.*?)">尾页</a>') #html?page=\d+

p2detail = re.compile(ur'<a name="\d+" href="(.*?)" target="_blank">(.*)</a>')

p2title = re.compile(ur'<title>专栏：(.*) - 博客频道 - CSDN.NET</title>')

p2titlereplace = re.compile(r'[\/:*?"<>|]')

def find_url_prefix_maxpage_title(content):
    title = p2title.findall(content,re.X)
    l =  p2first.findall(content,re.X)
    if l and len(l[0].split("=")) == 2:  #存在多页
       return True,l[0].split("="),title[0]
    else:
       return False,(None,None),title[0]

def get_request(url):
    #设置超时
    socket.setdefaulttimeout(60)
    #可以加入请求头信息，以便识别
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
                "Accept": "text/plain"}
    req = urllib2.Request(url, headers=i_headers)
    content = ""
    try:
        page = urllib2.urlopen(req)
        #print page.geturl()
        #print page.info().getplist()
        content =  page.read().decode("utf-8")
    except urllib2.HTTPError, e:
        print "Error Code:", e.code
    except urllib2.URLError, e:
        print "Error Reason:", e.reason
    return content

def gen_urls(url_prefix, max_page):
    for i in range(1,max_page+1):
        yield url_prefix + "=" + str(i)

def download_pages(url, dir_path):
    content = get_request(url)
    l =  p2detail.findall(content,re.X)
    #print l,len(l),l[0]
    for (detail_url, title) in l:
        print "Downloading: ",title,detail_url
        title, num = p2titlereplace.subn("-",title)
        path = dir_path + os.sep + title + ".html"
        if not os.path.exists(path): #只下载新文章，不过老文章修改无法下到，要想全部更新，可以去掉if
            f = open(path,"w")
            f.write(get_request(detail_url).encode("utf-8"))
            f.close()

def get_down(first_url):
    content = get_request(first_url)
    multi_page,(url_prefix, max_apge), title =  find_url_prefix_maxpage_title(content)

    print title
    title, num = p2titlereplace.subn("-",title)
    dir_path = "./"+title
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    if multi_page:
        for url in gen_urls(url_prefix, int(max_apge)):
            print url
            download_pages("http://blog.csdn.net" + url, dir_path)
    else:
        download_pages(first_url, dir_path)



if __name__ == '__main__':
    #first_url = "http://blog.csdn.net/column/details/novelnorains.html?page=4"
    # first_url = "http://blog.csdn.net/column/details/wklken4ds-alg-py.html"
    # get_down(first_url)
    # sys.exit(0)

    urls = [
    "http://blog.csdn.net/column/details/wklken4ds-alg-py.html", #数据结构和算法python实现,未完
    "http://blog.csdn.net/column/details/wklken4linux.html", #linux新手生存笔记，未完
    ]
    for first_url in urls:
        get_down(first_url)
# coding = utf-8
__author__ = 'apple'
__date__ = '2014-08-08 23:10'

#coding=utf8

import urllib2
import re

"""
Login to Sina Weibo with cookie
"""

#fill with your weibo.com cookie
COOKIE = 'SINAGLOBAL=2789640433620.6616.1359362777225; _s_tentry=weibo.com; Apache=1901955700013.7866.1366248813327; v5reg=usrmdins1024; appkey=; USRUG=usrmdins41453; login_sid_t=a65b1679bc9a6e6801fddec0b7945b5d; USRHAWB=usrmdins311196; YF-Ugrow-G0=cd9e8fbbed8e8c42cab38a5786ea18b7; YF-V5-G0=c2f54dafbe53b1d2f7183e51668d457a; YF-Page-G0=e1a5a1aae05361d646241e28c550f987; ULV=1403971983913:1:1:1:1901955700013.7866.1366248813327:; WBtopGlobal_register_version=ab49b31824b6dba1; wvr=5; SUS=SID-1650626260-1407500237-GZ-5rx6u-3fe44275b094656b179a5dcd3ac09b9c; SUE=es%3D9c661bcb1d0981921ec00d2b50804258%26ev%3Dv1%26es2%3D83aff6aa22f1a9979987cfd3937e6122%26rs0%3DZuHo2BqOCkUqw3ZPHg26DoDnL7LahlIZ70vGlQHDybcGTG0vTW92T33ODCCVd%252F%252BFDRq6gcqDuwgjxhizsgSnpYw3dJlsLZ8yueuwuJ%252BC56C5V2fiaNItSPcNOSXe2PICJ0B3IieE%252F3osSkc%252FwxnaI0PZ5WTsIcNdH0FA%252FWob%252Fts%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1407500237%26et%3D1407586637%26d%3Dc909%26i%3D9b9c%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D1650626260%26name%3Dpeter.wang.wh%2540gmail.com%26nick%3D%25E8%258D%2589%25E6%25B3%25A5%25E9%25A9%25AC%25E7%259A%2584%25E5%25A5%2587%25E8%25BF%25B9%26fmp%3D%26lcp%3D2014-04-10%252010%253A41%253A30; SUB=_2AkMkuDD6a8NlrAJXnfgTzm3gao1H-jyXboQMAn7uJhIyGxgf7lAKqSWbdASI5llJG4V00gxVNu_G1N9UAg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhkG6TFTO2AgBm9c9KYCOAD5JpX5KMt; ALF=1439036235; SSOLoginState=1407500237; UOR=tech2ipo.com,widget.weibo.com,www.leiphone.com'

HEADERS = {"cookie": COOKIE}

def test_login():
    url = 'http://weibo.com'
    req = urllib2.Request(url, headers=HEADERS)
    text = urllib2.urlopen(req).read()
    print(text)

    pat_title = re.compile('<title>(.+?)</title>')
    r = pat_title.search(text)
    if r:
        print r.group(1)


if __name__ == '__main__':
    test_login()
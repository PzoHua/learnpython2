#_*_coding=utf-8_*_
import urllib2

# 1.伪装浏览器
req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':None 
}


# 2.抓取网页
url = "http://gov-hack.lofter.com/"
req = urllib2.urlopen(url, None, req_header)
html = req.read()
print html

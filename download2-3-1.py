import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://hitomi.la/galleries/1404346.html"

mem = req.urlopen(url)

#print(type(mem))
#print(type({}))
#print(type([]))
#print(type(()))

#print("geturl", mem.geturl())
#print("status", mem.status) #200 정상, 404 없는 페이지, 403 리젝트, 500 서버 에러
#print("headers", mem.getheaders())

#print("info", mem.info())
#print("code", mem.getcode())
#print("read", mem.read(50).decode("utf-8")) #"euc-kr"

print(urlparse(url))

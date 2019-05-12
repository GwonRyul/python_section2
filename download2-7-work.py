from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

hotissue = soup.select("ol.list_hotissue.issue_row>li")

for e in range(0,10) :
    print(e+1,"위 ", hotissue[e].select_one('a').string, hotissue[e].select_one('a').attrs['href'])

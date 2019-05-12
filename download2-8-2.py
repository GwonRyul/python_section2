from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

opener = req.build_opener()
opener.addheaders = [('User-agent','Mozilla/5.0')]
req.install_opener(opener)

base = "https://www.inflearn.com/"
#quote = rep.quote_plus("고양이") # %EA%B3%A0%EC%96%91%EC%9D%B4 고양이
url = base #+ quote
#print(url)

res = req.urlopen(url)
savePath = "D:/Atom WorkSpace/imgedown/"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("div.slider_container")
for i, e in enumerate(img_list, 1) :
    #print(img_list['data-source'])
    with open(savePath+"text_"+str(i)+".txt","wt") as f:
        f.write(e.select_one("div.course_card_front > div.card-content > div.course_title"))
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    #print(fullFileName)
    req.urlretrieve(img_list['data-source'],fullFileName)

print("다운로드 완료")

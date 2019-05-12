import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://tn.hitomi.la/smallbigtn/1408273/1.jpg.jpg"
htmlURL = "https://google.com"

savePath1 = "D:/Atom WorkSpace/test1.jpg"
savePath2 = "D:/Atom WorkSpace/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)
print("다운로드 완료!")

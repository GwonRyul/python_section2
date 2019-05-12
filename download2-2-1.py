import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print('hi')

imgUrl = "https://tvetamovie.pstatic.net/libs/1231/1231649/b2ddc5448c15ce15397a_20190327222457437.mp4-pBASE-v0-f77333-20190327222621086_1.mp4"
htmlURL = "https://google.com"

savePath1 = "D:/Atom WorkSpace/test1.mp4"
savePath2 = "D:/Atom WorkSpace/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(imgUrl).read()

saveFile1 = open(savePath1, 'wb') # w: write r: read, a: add,
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")

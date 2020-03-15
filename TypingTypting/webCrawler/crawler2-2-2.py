import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imageUrl = "http://www.aitimes.kr/news/photo/201802/11399_11104_2850.jpg"
htmlUrl =  "http://www.aitimes.kr/news/articleView.html?idxno=11399"

savePath1 = "C:/Coding/test/publicdata2.jpg"
savePath2 = "C:/Coding/test/dataEnovation2.html"

f = req.urlopen(imageUrl).read()
f2 = req.urlopen(htmlUrl).read()

saveFile1 = open(savePath1, 'wb')
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

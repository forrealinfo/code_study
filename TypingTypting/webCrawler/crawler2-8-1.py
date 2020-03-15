from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = urllib.parse.quote_plus("연애인")
url = base + quote
print('url : ', url)
print()

res = urllib.request.urlopen(url)
savePath = 'C:/imagedawn2/'

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, 'html.parser')

img_list = soup.select("div.img_area._item > a.thumb._thumb > ._img")
print(img_list)
print()

for i, img_list in enumerate(img_list, 1):
    print(img_list['data-source'])
    fullFileName = os.path.join(savePath, savePath + str(i) + '.jpg')
    urllib.request.urlretrieve(img_list['data-source'], fullFileName)
print("다운로드 완료")

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 한글주소 변환
# base = "https://www.inflearn.com/"
# quote = urllib.parse.quote_plus("추천_강좌")
# url = base + quote
# print("url : ", url)

savePath = 'C:/imagedown3/'
base = "https://www.inflearn.com/courses/"
add = "it-programming/algorithm"
url = base + add
# print(url)

res = urllib.request.urlopen(url).read()
# print(res)

soup = BeautifulSoup(res, 'html.parser')

lec_names = soup.select('div.card-content > div.course_title')

print(lec_names)
print()

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!")
        raise

for i, lec_name in enumerate(lec_names, 1):
    print(i, lec_name.string)
    lec_text = '{}번 강의: {}'.format(i, lec_name.string)
    with open(savePath + 'title_' + str(i) + '.txt', 'wt') as f:
        f.write(lec_text)

lec_images = soup.select('div.card-image > figure.image.is_thumbnail > img')

for i, lec_image in enumerate(lec_images, 1):
    url = lec_image['src']

    # print(url)
    fullFileName = os.path.join(savePath, savePath + 'img_' + str(i) + '.png')
    urllib.request.urlretrieve(url, fullFileName)

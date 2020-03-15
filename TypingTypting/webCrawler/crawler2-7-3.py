from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 한글주소 변환
# base = "https://www.inflearn.com/"
# quote = urllib.parse.quote_plus("추천_강좌")
# url = base + quote
# print("url : ", url)

base = "https://www.inflearn.com/courses/"
add = "it-programming/algorithm"
url = base + add
# print(url)

res = urllib.request.urlopen(url).read()
# print(res)

soup = BeautifulSoup(res, 'html.parser')
algo_lec = soup.select('div.card-content > div.course_title')
# print(algo_lec)
for i, e in enumerate(algo_lec, 1):
    print('프로그래밍 > 알고리즘강의 {} : {}'.format(i, e.text))

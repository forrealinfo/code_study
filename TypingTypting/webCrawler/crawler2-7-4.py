from bs4 import BeautifulSoup
import urllib.request
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net/"
res = urllib.request.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')


# select를 태그, 속성값, 클래스를 복합적으로 사용하여 적용함.
best_click = soup.select('div.rank_cont[aria-hidden = true] a.link_issue')
# print(best_click)

for i, e in enumerate(best_click, 1):
    if i > 10:
        break
    print('다음 실시간 검색어 순위 {}위 : {}'.format(i, e.text))

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")

# html 또는 html(read) 모두가능
bsObj = BeautifulSoup(html, "html.parser")

# 'lxml' 'html5lib' 구문분석기도 사용가능, html 구문 능동수정
# bsObj = BeautifulSoup(html, 'lxml')
# bsObj = BeautifulSoup(html, 'html5lib')

# 파서에 의해 태그가 분석되어서 나옴
print(bsObj)

print('-----------------')
# 특성태그 추출
print(bsObj.h1)

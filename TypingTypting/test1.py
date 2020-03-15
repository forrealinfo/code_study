from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
# print(html.read())
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj)

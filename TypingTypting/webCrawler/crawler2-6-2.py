from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("C:/Coding/testRepo/TypingTypting/webCrawler/food-list.html", encoding = "utf-8") # 파이썬 내장함수 open
soup = BeautifulSoup(fp, "html.parser")

print(soup)

# select 는 tag리스트를 반환한다
print("1 : ", soup.select("li:nth-of-type(4)")[0].string)
print("1 : ", soup.select("li:nth-of-type(4)")[1].string)

# 오류발생
# print("1 : ", soup.select("li:nth-of-type(4)").string)

# select_one는 tag를 반환한다.
print("2 : ", soup.select_one("#ac-list > li:nth-of-type(4)").string)
print("3 : ", soup.select("#ac-list > li[data-lo='cn']")[0].string)
print("4 : ", soup.select("#ac-list > li.alcohol.high")[0].string)

for ac in soup.find_all("li"):
    if ac["data-lo"] == "us":
        print("data_lo == us : ", ac.string)
        

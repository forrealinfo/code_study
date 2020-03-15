# 2019-01-28 수정
# 기존 daum 주식 사이트 : ajax 방식으로 변경으로 인해 이를 반영한 코드를 수정.
# pip install fake-useragent 설치 후 실행 가능

import io
import json
import sys
import urllib.request
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Fake Header 정보
ua = UserAgent()

# 헤더 선언
headers = {
    "User-Agent": ua.ie,
    "referer": "'https://finance.daum.net/"
}

# 다음 주식 요청 url
url = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청
res = urllib.request.urlopen(urllib.request.Request(url, headers = headers)).read().decode("utf-8")

print("res : ", res)

# 응답 데이터 str -> json 변환 및 data 값 저장
rank_json = json.loads(res)["data"]

# 중간확인
print("중간 확인 : ", rank_json, "\n")

for elm in rank_json:
    #print(type(elm))
    print("순위 : {}, 금액 : {}, 회사명 : {}".format(elm["rank"], elm["tradePrice"], elm["name"]))

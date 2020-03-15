import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 로그인 유저정보
Login_Info = {
    'user_id': 'ssachin',
    'user_pw': 'tjrwjd1301'
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    login_req = s.post('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com', data = Login_Info)
    # html 소스 확인
    print('login_req', login_req.text)
    # Http Header 확인
    print('login_req', login_req.headers)

    # Response 정상 확인
    if login_req.status_code ==200 and login_req.ok:
        # 권한이 필요한 게시판 게시글 가져오기
        post_one = s.get('http://market.ruliweb.com/read.htm?table=market_ps&page=1&num=4623554&find=&ftext=')

        # 예외 발생
        post_one.raise_for_status()
        # print(post_one.text)

        # BeautifulSoup 선언
        soup = BeautifulSoup(post_one.text, 'html.parser')
        # print(soupprettify())

        article = sou.select_one('table:nth-child(1)').find_all('p')
        # print(article)

        for i in article:
            if i.span is not None and \
                    i.span.string is not None:
                print(i.span.string)

import sys
import io
import requests


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'https://www.gov.kr/nlogin/?Mcode=10003'
params = {'userID':'azajust' , 'pwd':'tjrwjd1301!'}

r = requests.post(url, params)
print(r.text)

import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url1 = 'https://www.naver.com'
res1 = requests.Session().get(url1)
print('1 : ', res1.text)

url2 = 'http://httpbin.org/cookies'
res2 = requests.Session().get(url2, cookies = {'from' : 'myName'})
print('2 : ', res2.text)


url3 = 'http://httpbin.org/get'
headers = {'user-agent' : 'myPythonApp_1.0.0'}
res3 = requests.Session().get(url3, headers = headers)
print(res3.text)

requests.Session().close()

url4 = 'https://www.naver.com'
with requests.Session() as ses:
    res4 = ses.get(url4)
    print(res4.text)

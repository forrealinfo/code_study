import requests
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Response 상태 코드
url = 'http://httpbin.org/get'
res = requests.Session().get(url)
print(res.status_code)
print(res.ok)

# https://jsonplaceholder.typicode.com

url2 = 'https://jsonplaceholder.typicode.com/posts/1'
res2 = requests.Session().get(url2)
print(res2.text)
print(res2.json())
print(res2.json().values())
print(res2.json().keys())
print('------------')
print(res2.encoding)
print('------------')
print(res2.content)
print(res2.raw)

import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# url = 'https://api.gitjub.com/events'
# res = requests.get(url)
# res.raise_for_status()
# print(res.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'kim', domain = 'httpbin.org', path = '/cookies')

res = requests.get('http://httpbin.org/cookies', cookies = jar)
res.raise_for_status()
print(res.text)

res = requests.get('https://github.com', timeout = 3)
print(res.text)

payload1 = {'key1' : 'value1', 'key2' : 'value2'}
payload2 = (('key1', 'value1'), ('key2', 'value2'))
payload3 = {'some' : 'nice'}

res = requests.post('http://httpbin.org/post', data = payload1) #form
print(res.text)

res = requests.post('http://httpbin.org/post', data = json.dumps(payload3))
print(res.text)

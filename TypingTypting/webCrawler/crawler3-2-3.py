import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'http://httpbin.org/stream/20'
res = requests.Session().get(url, stream = True)
print(res.text)
print(res.encoding)
# print(res.json())
if res.encoding is None:
    res.encoding = 'utf-8'

for line in res.iter_lines(decode_unicode = True):
    print(line)
    # b = json.loads(line) #dict
    # for e in b.keys():
    #     print("key : ", e, "values : ", b[e])

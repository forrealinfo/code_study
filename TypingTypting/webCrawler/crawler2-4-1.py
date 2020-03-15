import os
import subprocess

import pytube

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

yt = YouTube('https://www.youtube.com/watch?v=FM_3-PBk8eo&t=996s')
vids = yt.streams.all()
print('vids : ', vids)

### 현재 pytube 에러로 인해 버그수정후 추후 새로운 파일이 업로드 된후 사용할것.

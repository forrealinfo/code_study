# Chapter03_02
# 팡이썬 문자형

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 문자열 생성
str1 = "I am Python."
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 문자열 출력
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

# 문자열 길이
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널문자
'''
"""

escape_str1 = "Do you have a \"retro games\"?"
escape_str2 = 'What\'s on TV?'

# 출력1
print(escape_str1)
print(escape_str2)

# 탭, 줄바꿈
t_s1 = "Click\tStart!"
t_s2 = "New Line\nCheck!"

# 출력2
print(t_s1)
print(t_s2)

# Raw String
raw_s1 = r'D:\Python\python3'
raw_s2 = r"\\x\y\z\q"

# Raw String 츨략
print(raw_s1)
print(raw_s2)

multi_str1 = \
    """
    문자열
    멀티라인 입력
    테스트
    """
# 멀티라인 출력
print(multi_str1)

multi_str2 = \
    '''
    문자열 멀티라인
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 문자열 연산
str_01 = "Python"
str_02 = "Apple"
str_03 = "How are you doing?"
str_04 = "Seoul Deajeon Busan Jinju"

print(3 * str_01)
print(str_01 + str_02)
print(dir(str_01))
print('y' in str_01)
print('n' in str_01)
print('p' not in str_02)

# 문자열 형 변환
print(str(66))
print(str(10.1))
print(str(True))
print(str(complex(12)))

# 문자열 함수 (upper, isalnum startswith, count, endswith, isalpha 등)
print("Capitalize: ", str_01.capitalize())
print("endswith?: ", str_02.endswith("s"))
print("endswith?: ", str_02.endswith("e"))
print("join str: ", str_01.join(["I'm ", "!!!"]))
print("replace1: ", str_01.replace('thon', 'Good'))
print("repalce2: ", str_03.replace("are", "was"))
print("split: ", str_04.split(' ')) # Type 확인
print(type(str_04.split(' ')))
print("sorted: ", sorted(str_01)) # Reverse = True
print("sorted: ", sorted(str_04))
print("reversed1: ", reversed(str_02)) # List 형 변환
print("reversed2: ", list(reversed(str_02)))
print(list(str_01))


# 반복(시퀀스) 설명
im_str = "Good Boy!"
print(dir(im_str)) # __iter__확인

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = 'Nice Python'

# 슬라이싱 연스
print(str_s1[0:3])
print(str_s1[:len(str_s1)])
print(str_s1[:len(str_s1) - 1])
print(str_s1[:])
print(str_s1[1:4:2])
print(str_s1[-4:-2])
print(str_s1[1:-2])
print(str_s1[::-1])
print(str_s1[::2])

# 아스키코드
a = 'z'
print(ord(a))
print(chr(122))

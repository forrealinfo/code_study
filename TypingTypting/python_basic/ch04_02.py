# Chapter04-02
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for i in <collection>
#       <loop body>

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

for v1 in range(10):
    print("v1 is : ", v1)

print()

for v2 in range(1, 11):
    print("v2 is : ", v2)

print()

for v3 in range(1 ,11, 2):
    print("v3 is : ", v3)

print()

# 1 ~ 1000 합

sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 Sum : ', sum1)

print('1 ~ 1000 Sum : ', sum(range(1, 1001)))  # sum(리스트)

print('1 ~ 1000 안에 4의 배수의 합 : ', sum(range(1, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 에제1
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

for name in names:
    print("You are ", name)

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
    print("Current number : ", number)

# 예제3
word = 'Beautiful'

for s in word:
    print('word : ', s)

# 예제4
my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}

for i in my_info:
    print(i, ":", my_info[i])

for val in my_info.values():
    print(val)

# 예제5
name = "FineApplE"

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# break
for num in numbers:
    if num == 34:
        print("Found : 34!")
        break
    else:
        print("Not found : ", num)

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type : ", type(v))
    print("multiple by 2 : ", v * 3)

# else 구문 예제1
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:  # 45
        print("Found : 34!")
        break
else:
    print("Not Found 45...") #마지막에 반드시 한번은 실행하도록하는 구문

# else 구문 예제2
for num in numbers:
    if num == 45:  # 45
        print("Found : 34!")
        break
else:
    print("Not Found 45...")

# 구구단 출력
for i in range(1, 10):
    for j in range(1, 10):
        print('구구단 {}단 : {} * {} = {}'.format(i, i, j, i*j), end = ' / ')
    print()

# 변환 예제
name = 'Aceman'
print('Reversed : ', reversed(name))
print('List : ', list(reversed(name)))
print('Tuple : ', tuple(reversed(name)))
print('Set : ', set(reversed(name)))  # 순서X


# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -->Method 선언
# Pascal Case : NumberOfCollegeGraduates  -->Class 선언
# Snake Case : number_of_college_graduates -->파이썬의 일반적인 변수선언
print('-------------------------------------------------------------')

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a -', a)

a.insert(2, 7) # 몇번째 순서에 어떤 값을 넣어라
print('a - ', a)

print('a - ', a.index(5)) # a 리스트에서 ()어떤 겂이 몇번째에 있는가.

print('a - ', a.count(4)) # a 리스트에서 ()어떤 값의 개수가 몇 개인가

a.sort()  # a 리스트를 오름차순 정렬
print('a - ', a)
print('-------------------------------------------------------------')
# 튜플 연산
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)

print('-------------------------------------------------------------')
# print(type(true)) #소문자 true로 하면 오류발생
print(type(True))

print('-------------------------------------------------------------')
# CH04_02.py
# 딕셔너리 반복문 형태
my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}

for i in my_info:
    print(i, ":", my_info[i])

for i in my_info.values():
    print(i)

print('-------------------------------------------------------------')
# 구구단 출력
for i in range(1, 10):
    for j in range(1, 10):
        print('구구단 {}단 : {} * {} = {}'.format(i, i, j, i*j), end = ' / ')
    print()

print('-------------------------------------------------------------')

# *args   복수의 인자를 받고자하는 경우, 튜플로 반환
def args_func(*args):
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

print('-------------------------------------------------------------')

# **kwargs(언팩킹)  복수의 인자를 딕셔너리형태로 받는 경우
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])

kwargs_func(name1 = 'Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho')

print('-------------------------------------------------------------')
# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1=20, age2=30, age3=40)

print('-------------------------------------------------------------')

# 중첩함수
# 호이스팅의 원칙에 따라 변수선언 등 먼저 읽고 개별 함수의 실행은 나중에 실행.

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)

#  func_in_func(1000) 내부함수를 외부에서 직접 실행불가

print('-------------------------------------------------------------')

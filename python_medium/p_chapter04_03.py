# Chapter04-03
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# Dict 구조
# print(__builtins__.__dict__)

print()
print()

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print( hash(t1))
# print(hash(t2)) # 예외발생

print()
print()

# Dict Setdefault 예제
source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)  #딕셔너리는 append 함수사용못하지만, 이경우는 딕셔너리 내부의 value 값이 리스트로 구성되어 있음으로 리스트에 append함수를 적용하는 것이 된다.
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의
new_dict3 = {k : v for k , v in source} #이 경우는 키 값이 동일한 경우 나중의 value값으로 덮어써버리는 문제가 생긴다.

print(new_dict3)

print()
print()

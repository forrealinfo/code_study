# chapter 5-2
# 파이썬 사용자 입력
# input 사용법
# 기본 타입(str)

# 예제1
name = input('enter your name :')
grade = input('enter your grade :')
company = input('enter your company name :')

print(name, grade, company)

# 예제 2
number = input('enter number :')
name = input('enter name :')

print('type of number', type(number), number * 3)
print('type of name', type(name))

# 예제3(계산)
first_number = int(input('enter number1 :'))
second_number = int(input('enter number2 :'))

total = first_number + second_number
print('first_number + second_number : ', total)

# 예제4
float_number = float(input('enter a float number :'))

print('input float : ', float_number)
print('input type : ', type(float_number))


# 예제5
print('firstname - {0}, lastname - {1}'.format(input('enter first name :'), input('enter second name :')))

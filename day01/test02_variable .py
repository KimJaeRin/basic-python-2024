# date: 20240129
# desc: 자료형

## 기본자료형 - 숫자형, 문자형, 불형, None형...
## 추가자료형 - 리스트형, 튜플형, 딕셔너리, 집합...

## None형 == null(C, C++, C#, Java, SQL)
## 값은 값인데 아무것도 지정할 수 없는 값 => None

apple = None
print(apple)

## 숫자형 -정수형, 실수형, 진수형
### 정수
ten = 10
hundred = 100
temp = -8

### 실수
pi = 3.141592
tax_rate = 10.0
emp_earn_rate = 3.3
test_val = 2e10
print(test_val)

### 진수 (2, 8, 16진수)
bit142 = 0b10001110 # 0 => 0, 1 => 1, 10 => 2, 11 => 3, 100 => 4, 101 => 5, 110 => 6, 111 => 7, 1000 => 8
oct9 = 0o11 #1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20, ..., 77, 100
hex255 = 0xFF  #0, 1, 2, 3, 4, 5, 6, 7, 8, 9,A, B, C, D, E, F

print(bit142)
print(oct9)
print(hex255)

## 문자형 - 파이썬에는 문자, 문자열 차이 X
greeting = 'Hello!'
greeting = "Hello!" #홑따옴표, 쌍따옴 표 모두 문자열을 나타냄
print(greeting)
multi_str = '''Hello
I am a programmer.
Have a good afternoon.'''
print(multi_str)  # " "도 똑같이 적용.

multi_str2 = ('Line1\n'
              'Line2\n'
              'Line3')
print(multi_str2)


multi_str2 =  'Line1\n'  \
              'Line2\n'  \
              'Line3'   # ()을 다 쓰거나, 문장 끝마다 \ 붙이기
print(multi_str2)


## 불형 (Bool, Boolean)

















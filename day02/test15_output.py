# file : test15_output.py
# desc : 콘솔출력 포맷양식(String format)

string_1 = '{}'.format(10) #{} 위치에 함수 뒤애 들어있는 값을 치환, 원하는 양식으로 표현
print(type(string_1))

name = '재린'         #input('이름 입력 > ')
string_2 = '안녕하세요, {}입니다!'.format(name)
print(string_2)

string_3 = '{} {} {}'.format(4000, '만', '빌려주세요')
print (string_3)

#정수를 문자열 포맷
# = : 기호와 숫자를 분리, 05: 다섯자리 만들때 빈자리 0으로 채우기, d : 정수
string_4 = '______{:d}_____'.format(100) #앞에 스페이스
print(string_4)

#실수 문자열포맷 f = 기본 소수점 6자리

string_5 = '_____{:7.2f}_____'.format(78.333333333333)
print(string_5)

# 파이썬 3.6 이후 도입 format 함수 아예 사용안함
val = 78.33333333
string_6 = f'________{val:7.2f}_________'
print(string_6)

string_7 = 'Hello, World!'
print(string_7.upper()) # upper 모두 대문자로 변환
print(string_7.lower()) # 모두 소문자로 변환
print(string_7.lower().capitalize()) # cap 첫 글자만 대문자로

print(string_7.split(' '))  # 특정한 단어로 자르는 함수

string_8 = 'Hello, I am Jae Rin. I am a student. Good Luck for your day.'
words = string_8.split(' ')
print(words)
print(f'문장 단어 갯수는{len(words)} 개 입니다.')


string_9 = 'A10'
print(string_9.isalnum()) #True
print(string_9.isnumeric()) #False

string_10 = '-10.5' #소수점은 함수를 만들어서 처리
print(string_10.isdigit()) #decimal - 정수

print('안녕' in '안녕하세요') #문장안에 단어가 있는지 확인 T/F로 나옴




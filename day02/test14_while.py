# file : test14_while.py
# desc : while 문

## while 참인조거:
## 공통점 if 조건:elif 조건: else: for in range():, while 조건:

count = 0


#while count <  10:  # count 변수값이 10보다 작거나 같은동안 반복
#무한루프 : Window OS , Mobile OS, 자동차 네비게이션, 라즈베리파이, 아두이노, 게임, Winform 개발, ...
           
# while True : #참인동안 True 항상 참(infinite Loop)
#     count = count + 1
#     print('나무찍기', count)
#     if count == 10:
#         break #이 반복문을 빠져나가라

number = 1
while True :
    number = number + 1
    if str(number).count('3')  == 1 or \
        str(number).count('6')  == 1 or \
        str(number).count('9')  == 1 : #숫자를 문자열로 바꾼 값안에 3,6,9가 있으면
        print('짝!') #continue 는 반복에서 제외, break는 반복문 완전히 빠져나가는 것
        
    else:
        print(number)

    if number == 30:
        break   




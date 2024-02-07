
number = int(input('구구단을 수행 할 숫자 입력 : '))

for i in range(1,10):
    print(f'{number} x {i} = {number*i}',end = ' , ')  #2d = 오른 쪽 정렬 , end = 엔터대신 공백으로 변경
   
    
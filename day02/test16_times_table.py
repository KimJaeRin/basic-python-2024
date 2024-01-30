# file : test16_times_table.py
# desc : 구구단 프로그램
# spec : for문 잘 써야함, 2중 for문의 이해
# debugging = F9(중단점 토글), F5(디버깅 시작), F10(한줄씩 실행), F11(함수안으로 진입)
#shift + F5 = 디버깅 종료
# x * y = x*y

print('구구단 시작')
for x in range(2,10):
    print(f'{x}단------->')
    for y in range(1,10):
        print(f'{x} x {y} = {x*y:2d}',end = ' , ')  #2d = 오른 쪽 정렬 , end = 엔터대신 공백으로 변경
    print() #안 쪽 For문이 끝나면 마지막엔터를 하나 추가


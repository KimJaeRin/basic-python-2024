# data : 20240131
# file : test17_input.py
# desc : 콘솔입력

# input()
# 출력 - 컴퓨터 화면, 프린터, 스피커, 빔프로젝터, VR
# 입력 - 콘솔입력(키보드), 마우스 입력, 목소리, 오큘러스, 조이스틱, 터치 스크린
# input('내용추가) 반드시~!

#temp_val = input('곱할 수 입력 :')
#temp_val = int(temp_val)  # 문자열형에서 정수형으로 변환 (형 변환)
#temp_val = int(input('곱할 수 입력 :'))  # 위의 주석 코드 변환 가능
temp_val = input('곱할 수 입력 :')
if temp_val.isnumeric() == True:   # 숫자입력이 아니면 튕겨냄 
    temp_val = int(temp_val)  # 문자열형에서 정수형으로 변환 (형 변환)
    print(f'입력값 = {temp_val}')

# 곱하기
    result = temp_val*5
    print(f'결과 = {result}')
else:4
    print('정수만 입력하세요.')
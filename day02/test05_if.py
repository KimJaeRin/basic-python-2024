# date : 20240130
# desc : 흐름제어 if

## 어떤 조건이 참일때와 거짓일때로 나누어서 어떤 일을 처리하는 것.
## if 조건: - 참인 조건
## else 조건: - 거짓인 조건
## 입력 - input()
number = int(input('정수 입력  > ')) # 문자로 된 입력값을 정수로 변경.

if number > 0:
    print('양수입니다.')
elif number == 0:
    print('0입니다.')
elif number < 0:
    print('음수 입니다.')
else:
    print('정의할 수 없습니다.')




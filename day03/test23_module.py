# file : test23_module.py
# desc : 모듈 사용
import math

PI = 3.141592
radius = 5
print(f'원의 크기는 {radius * radius * PI}')
# print(math.pi)
print(f'정확한 원의 크기는 {radius * radius * math.pi}')

print(f'cos(0) = {math.cos(0)}')
print(2**10)
print(math.pow(2,10))
print(math.ceil(3.1)) #올림
print(math.floor(3.5)) #내림
print(round(3.5)) #반올림(math에 포함 x)

import math as m  #별명 짓ㄱㅣ
print(m.sin(30))

from math import pi, pow #math 중 2개만 import

print(pow(2,10))







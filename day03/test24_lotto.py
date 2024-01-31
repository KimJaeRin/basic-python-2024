# file : test24_lotto.py
# desc : 로또번호 생성

import random as rnd # 랜덤은 주로 rnd로 줄임

# numbers = list(range(1,46))
# # print(numbers)

# lottery = list()

# for i in range(6):
#     lottery.append(rnd.choice(numbers))
# print(lottery)

numbers = weight = list (range(1,46))
lottery = list()
rnd.shuffle(weight)

lottery = rnd.choices
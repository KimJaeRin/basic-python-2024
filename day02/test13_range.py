# file : test13_range.py
# desc : 리스트 범위지정

list_a = [1,2,3,4,5,6,7,8,9,10]

print(list_a)

#범위 지정 range(n, 0부터 n개의 범위 수를 생성)

print(range(5))
print(list(range(5)))
print(list(range(1,6)))
print(list(range(2,21,2))) # 2 부터 20까지 2씩 증가 
print(list(range(10,-1,-1)))

list_a = list(range(1,101)) # 리스트 컨프리헨션
print(list_a)






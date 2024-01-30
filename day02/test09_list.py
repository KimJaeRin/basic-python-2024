# desc : 복합 자료형 list
# 총 갯수 n 이면 index 마지막 값은 n-1
std = [80, 90, 100, 50, 60, 55, 77, 88, 99, 100]

# 리스트 요소 접근
print(std[8])

list_1 = [265, 3.5, '문자열', True, [1, 2, 3, 4 ],(1, 2), std]
print(list_1)
print(list_1[3])
list_1[6] = '바꾼 값'  # 리스트 요소 변경
print(list_1)

## 리스트 연산
print(list_1[2:4]) # : 뒤의수는 출력하고 싶은 인덱스 + 1

print(list_1[-1])

## 이중 리스트
print(list_1[4][2])  #[1, 2, 3, 4]중에서 3만 가져오기

list_2 = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2[1][2]) # 6

list_4 = [1,2,3]
list_5 = [7,8,9]

## 리스트 연산

print (list_4 + list_5)
print (list_4 * 2)

##리스트 길이
print(len(list_1))

## append() - 리스트 마지막에 하나 추가
## insert(index, val) - 리스트 index 이후에 val 추가
print(list_1)
list_1.append('hello')
print(list_1)

list_1.insert(2, 100) # 원래 값을 뒤로 미룸
print(list_1)

## extend() - 기존 리스트 확장

list_4.extend(list_5)
print(list_4)


## 리스트 삭제

del list_4[3]
print(list_4)

#del list_4 - 리스트 자체를 삭제

print(list_5)
val = list_5.pop() #마지막 값을 꺼내오기
print(val)
print(list_5)

# clear()
list_5.clear()
print(list_5) # del은 완전삭제 clear는 내용만 삭제

#sort() - 문자열, 숫자, 불 섞여있는 리스트는 정렬 안됨

std.sort() # 오름차순 정렬
print(std)

std.sort(reverse = True) # 내림차순 정렬
print(std)

#in, not in
print(99 in std) # True
print(98 in std) # False

#reverse(), copy(), count(),...

# *리스트 : 전개연산자

lsit_a = [1,3,5]
lsit_b = [2,4,8]
lsit_c = [*lsit_a, *lsit_b]
print(lsit_c)






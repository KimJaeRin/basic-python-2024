from collections import Counter


str =input('문자열을 영어로 입력하세요 : ')

str2 = str.split()

print(f'단어의 갯수는 : {len(str.split())}')

for i in range(len(str2)):
    if i % 2 != 0:
        result = str2[i].upper()
    else:
        result = str2[i]
    
    print(result,end=' ')



       

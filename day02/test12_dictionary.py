# file : test12_dictionary.py
# desc : 복합자료형 딕셔너리

## 사전형 - key와 value쌍을 나열해 놓은 자료형
# {key: value, key:value, key:value,...}

dict_movie = {'name': '어벤저스 엔드게임', 'type' : '히어로 무비',
              'year' : 2019, 'direcotor':'루소', 'cast' : ['아이언맨', '타노스', '헐크'] }
# 조회
print(dict_movie['year'])
print(dict_movie['cast'])

#추가, 수정
dict_movie['year'] = 2020
print(dict_movie)

dict_movie['producer'] = '케빈 파이기'
print(dict_movie)

#키에대한 값을 찾아낼 때
if 'musician' in dict_movie:
    print(dict_movie['musician'])
else:
    print('음악감독 없음')

musician = dict_movie.get('musician')
print(musician)    

# 반복문으로 출력
print('------------------------------------------------------------------------')
for key in dict_movie:
    print(key,':',dict_movie[key])
print('------------------------------------------------------------------------')

for key, value in  dict_movie.items():
    print(key, ':', value)




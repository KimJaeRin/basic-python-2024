# data : 20240131
# file : test19_starprint.py
# desc : 별 찍기 or 피라미드 만들기

for i in range(1, 6):
    #i가 1 일때는, range(1,2), 1번 반복
    #i가  2 일때는, range(1,3), 2번 반복
    for j in range(1, 6-i+1): 
        print(' ', end ='') # 엔터대신 empty로 변환
    

    for j in range(1, i+1):
        print('*', end ='')
    print()  #안 쪽 for문이 끝나면 엔터   






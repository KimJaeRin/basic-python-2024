# file : test28_fileio.py
# desc : 텍스트 파일 입출력

# mode : a(ppend : 추가) , r(ead: 읽기), w(rite : 파일 쓰기)
# encoding : cp949(= euc-kr : 한국어), utf-8(만국공통어)
f = open(r'sample.txt',mode='w', encoding='utf-8')


#.......... write()에서 엔터를 추가하려면 마지막에 \ㅜ 추가
f.write('안녕하세요. 우리는 IoT개발자 과정입니다.\n') # mode가 a 또는 w 일때 가능
f.write('반갑습니다')

f.close() #파일은 무조건 마지막에 닫는다.
print('파일이 생성되었습니다')

# file : test29_fileio.py
# desc : 텍스트 파일 읽기

f  = open('README.md',mode='r',encoding='utf-8')
#아래의 방법은 기본적이나 용량문제로 큰 파일은 읽기가 불가.
# text = f.read() #텍스트 파일의 모든 텍스트를 전부 한번에 읽어온다.
# print(text)

#아래는 가장 일반적.
while True:
    line = f.readline()
    if not line: break # 조건문이나 반복문 내의 코드가 한줄만 있으면 if 옆에 바로 적기 가능.
    print(line.replace('\n','')) #한줄식 띄우는거 없엠


f.close()




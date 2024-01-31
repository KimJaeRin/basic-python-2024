# basic-python-2024
부경대 2024IoT 개발자 과정 기초 프로그래밍 언더 - 파이썬


## 1일차
- 개발환경 구축
  - 코딩폰트 - 나눔고딕코딩
  - Notepad++ 설치
  - Python 설치
  - Visual Studio Code 설치
  - Git 설치
    - TortoiseGit 설치
    - Github 가입
    - Github Desktop 설치
    
- 파이썬 기초
  - 콘솔출력
  - 주석
  - 변수
  - 자료형
  - 연산자 

  ```python
  # 이 부분은 주석입니다.
  var_01 = 10 # 정수, 실수, 불, 문자열 모두 가능
  print(var_01)  #10
  print(type(var_01))  # class of int

  print(5 + 4/ 2) #7.0
  print(5 == 4) #False
  ```
  
## 2일차
- 파이썬 기초
  - 흐름제어
    - if : 참 / 거짓으로 조건 분기 (다른언어 switch)
    - for : 반복문 기본 (다른언어 foreach)
    - while : 반복문 변형 (다른언어 do~while)
  - 복합자료형 + 연산자(연산함수)
    - 리스트, 튜플, 딕셔너리
  - 출력 Format
  - 구구단 + 디버깅
  ```python
  print('구구단 시작')
  for x in range(2,10):
    print(f'{x}단------->')
    for y in range(1,10):
        print(f'{x} x {y} = {x*y:2d}',end = ' , ')  #2d = 오른 쪽 정렬 , end = 엔터대신 공백으로 변경
    print() #안 쪽 For문이 끝나면 마지막엔터를 하나 추가
    # debugging = F9(중단점 토글), F5(디버깅 시작), F10(한줄씩 실행), F11(함수안으로 진입)
    #shift + F5 = 디버깅 종료
    # x * y = x*y

  ```

## 3일차
- 파이썬 기초
  - 입력 방법
  - 별찍기
  - 함수, 람다함수는 나중에
  - 객체지향 (oop) 객체는 다 다름 변수와 함수의 조합 = class
    - 객체는 명사와 동사의 집합
    - 변수와 함수를 모두 모아둔 곳 : class
    - 클래스에서 하나씩 생성 : 객체 (object)
    - 캡슐화(__plateNumber)
- 패키지

  - 객체지향(나중에...)
    - 오버로딩, 오버라이딩(재정의)
    - 상속, 다중상속
    - 추상클래스, 인터페이스 ...
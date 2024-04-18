# data : 20240131
# file : test21_oop.py
# desc : 객체지향 클래스 만들ㄱ ㅣ

# 클래스(사람이라는 객체를 만들기위한 청사진) 만들기
class Person: #사람 클래스 선언
    name = ''  #멤버 변수
    age = 0
    gender = ''
    
    #생성자 함수 (스페셜 함수) 클래스의 객체를 생성할 때 동작.
    def __init__(self) -> None:
        self.name = '홍길동'
        self.age = 29
        self.gender = '남자'

    #클래스를 호출할 때 원하는 형태로 변환해서 보여줄 때    
    def __str__(self) -> str:
        strs = f'커스텀 출력, 이름 {self.name} 객체 생성!'
        return strs
    
    def walk(self):  # 멤버함수 매개변수 self 필수!
        print(f'{self.name}이(가) 걷습니다.')
    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

# 사람 객체 생성, Instance(사례, 예제)

jr = Person()  #함수호출처럼 작성하면 됨
es = Person()  

#print(type(jr))
#print(id(jr)) # 다른 객체인지 확인할 때 사용
#print(id(es))


jr.name = '김재린'   #객체명.멤버변수 =...
jr.age = '27'
jr.gender = 'man'

es.name = '애슐리'
es.age = '32'
es.gender = 'w'

print(f'jr => 이름: {jr.name} / 나이: {jr.age} / 성별: {jr.gender}')
print(f'es => 이름: {es.name} / 나이: {es.age} / 성별: {es.gender}')

jr.walk()
print('1분동안 걷는다')
jr.stop()

es.walk()
print('걷기 싫어함')
es.stop()

gd = Person()
print(f'gd => 이름: {gd.name} / 나이: {gd.age} / 성별: {gd.gender}')
print(gd)






 
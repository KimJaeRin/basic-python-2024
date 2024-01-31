# data : 20240131
# file : test22_car.py
# desc : Car Class 만들ㄱㅣ

class Car:
    wheel_num = 4
    color = 'White'
    __plate_num = ''
    company = ''
    gear_type = ''

    #전진, 후진, 우회전, 좌회전
    def moveForward(self):
        print(f'{self.__plate_num}이 전진합니다.')

    def moveBackward(self):
        print(f'{self.__plate_num}이 후진합니다.')

    def moveLeft(self):
        print(f'{self.__plate_num}이 좌회전합니다.')
    
    def moveRight(self):
        print(f'{self.__plate_num}이 우회전합니다.')

        #명사 - 변수, 동사 - 함수
    def __init__(self, plate_num, company , color, gear_type) -> None:
        self.__plate_num = plate_num
        self.company = company
        self.color = color
        self.gear_type = gear_type

    def __str__(self) -> str: # print(객체) 출력되는 부분
        return f'제 차는 {self.__plate_num}입니다. {self.color}입니다.'
        
    def getplatenumber(self): #외부에서는 접근할 수 없도록 막는 조치
        return self.__plate_num
    def setplatenumber(self, new_plateNumber):
        self.__plate_num = new_plateNumber

ren = Car('157하 1596','현대','흰색','자동')

# 객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수 있ㅇㅡㅁ. '__' 사용하면 객체에서만 변경가능 
print(ren)
print(f'차 번호는 {ren.getplatenumber()}')
print(f'차 색상는 {ren.color}')


ren.__plate_num = '234하 2323'  #변경 불가능
print(ren)




# csuv = Car('경남 99 1922', '기아','회색','자동')
# print(f'차 번호는 {csuv.__plate_num}')
# print(f'차 색상는 {csuv.color}')

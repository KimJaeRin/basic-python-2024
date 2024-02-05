# file : test36_PyQt
# desc : 기본화면 만들기

# print(sys.argv) #현재 파이썬 파일의 경로표시
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget # * = 모든걸 가져온다

class qtwin_exam(QWidget):   #QWidget을 상속, 모든 것 사용 가능 하다는 뜻
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()   #화면 초기화 함수 호출
    
    def initUI(self):
        self.setGeometry((1920-400)//2, (1080-300)//2, 400,300) # x, y, w, h
        self.setWindowTitle('Qt5 Hellow World!')
        self.text= ''
        self.show()

    def drawText(self, event, paint):
        paint.setPen(QColor(10,10,10,))   # r,g,b   000 = black  255,255,255 = white
        paint.setFont(QFont('NanumGothic', 15)) 
        paint.drawText(300//2,300//2,'Hell World')
        paint.drawText(event.rect(), Qt.AlignLeft,self.text)

    def paintEvent(self, event) -> None:
        paint = QPainter() 
        paint.begin(self)
        self.drawText(event,paint)
        paint.end()                          

loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성
isinstance = qtwin_exam() # Qwidget을 상속한 qtwin_exam 객체를 생성
loop.exec_()       


# file : test41_exam.py
# desc : # PyQt5로 이미지 뷰어


import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget


class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        # 이미지 추가 scaledToWidth로 해상도 고정
        pixmap = QPixmap('./images/cat.jpg').scaledToWidth(400)

        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)
        lblSize = QLabel(self)
        lblSize.setFont(QFont('나눔고딕',20)) # 폰트, 폰트 사이즈
        lblSize.setStyleSheet('color:#566C5D;')
        lblSize.setText(f'{pixmap.width()} x {pixmap.height()}') # cat.jpg의 width x height
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # 가로 중앙 정렬 | 세로 중앙 정렬
        vbox = QVBoxLayout(self) # 버티컬 레이아웃 위젯 생성
        vbox.addWidget(lblImage)  # VL에 위젯 추가
        vbox.addWidget(lblSize)
        self.setLayout(vbox) # form에 VL추가와 동일

        self.setWindowIcon(QIcon('./images/IOT.png'))
        self.setWindowTitle('이미지 뷰어')
        rect = QRect(300,300,300,300)
        self.setGeometry(rect)
        # self.setGeometry(300, 300, 300, 300) 오버로딩 함수
        self.setCenter()            #sfsf
        self.show()            #showFullScreen() 

    def setCenter(self): ## 윈앱을 화면 정중앙에 위치
        gm = self.frameGeometry() #윈앱 자신 위치 값
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    width, height = screen_rect.width(), screen_rect.height()
    print(width,' x ', height)
    ins = WinApp()
    
    sys.exit(app.exec_()) 


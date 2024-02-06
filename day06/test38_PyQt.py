# file : test38_PyQt.py
# desc : Qt디자이너로 만든 UI와 연동

# print(sys.argv) #현재 파이썬 파일의 경로표시
import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class qtwin_exam(QWidget):   
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/TestApp.ui',self) #QtDesigner에서 만든 ui를 로드
        #버튼에 대한 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) #ui파일내에 있는 함수명은 VSCode상에서 색상으로 표시x

        self.btnStop.clicked.connect(self.btnStopClicked)

    def btnStartClicked(self):
        print('시작버튼 클릭')
        self.lblstatus.setText('상태: 동작시작')
        QMessageBox.about(self,'동작','***시스템이 시작되었습니다')    
    
    #QWidget에 있는 closeEvent를 그대로 쓰면 그냥 닫힘
    #닫을지 말지를 한번 더 물어보는 형태로 다시 구현(재정의:Override)
    def btnStopClicked(self):
        print('종료버튼 클릭')
        self.lblstatus.setText('상태: 동작중지')
            
    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self,'종료확인','     종료할?',QMessageBox.Yes|QMessageBox.No) 
        if re == QMessageBox.Yes: 
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':
    loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성
    instance = qtwin_exam() # Qwidget을 상속한 qtwin_exam 객체를 생성
    instance.show()
    loop.exec_()       


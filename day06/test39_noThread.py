# file : test39_noThread.py
# desc : Qt에서 쓰레드 없이 동작 테스트
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
        uic.loadUi('./day06/ThreadApp.ui',self) #QtDesigner에서 만든 ui를 로드
        #버튼에 대한 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) #ui파일내에 있는 함수명은 VSCode상에서 색상으로 표시x

    def btnStartClicked(self):
        maxVal = 1000
        print('시작버튼 클릭')
        self.pgbTask.setValue(0) #프로그레스 바 0부터 시작
        self.pgbTask.setRange(0,maxVal-1) # 0 부터 100까지
        for i in range(maxVal): #0부터 100까지
            print_str = f'노쓰레드 출력 >>{i}'
            print(print_str)
            self.txbLog.append(print_str) 
            self.pgbTask.setValue(i)
            
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


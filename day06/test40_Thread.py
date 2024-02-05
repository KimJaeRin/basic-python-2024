# file : test40_Thread.py
# desc : Qt에서 쓰레드로 동작


import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class BackWorker(QThread):  #PyQt에서 스레드 클래스 상속 
    initSignal = pyqtSignal(int) #시그널을 UI스레드로 전달하기위한 변수객체
    setSignal = pyqtSignal(int) 
    setLog = pyqtSignal(str)

    def __init__(self, parent) -> None:
        super().__init__(parent) #부모 쓰레드에 있는 초기화 그대로 사용
        self.parent = parent #BackWorker에 사용할 멤버변수


    def run(self) -> None:  #쓰레드 실행
        #쓰레드로 동작 할 내용
        maxVal = 1000001
        self.initSignal.emit(maxVal)
        self.parent.pgbTask.setValue(0) #프로그레스 바 0부터 시작
        self.parent.pgbTask.setRange(0,maxVal-1) # 0 부터 100까지
        for i in range(maxVal): #0부터 100까지
            print_str = f'쓰레드 출력 >>{i}'
            print(print_str)
            self.setSignal.emit(i)
            self.setLog.emit(print_str)
            ###self.parent.txbLog.append(print_str) 
            ###self.parent.pgbTask.setValue(i)
            
class qtwin_exam(QWidget):   
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui',self) #QtDesigner에서 만든 ui를 로드
        #버튼에 대한 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) #ui파일내에 있는 함수명은 VSCode상에서 색상으로 표시x

    def btnStartClicked(self):
       th = BackWorker(self)
       th.start()  #Back내의 self.run()실행
       th.initSignal.connect(self.initPgbTask) #쓰레드에서 초기화 시그널이 오면 initPgbTask 슬롯함수가 대신 처리
       th.setSignal.connect(self.setpgbTask)
       th.setLog.connect(self.setTxbLog) # 텍스트브라우저 진행상황 출력
    
    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self,'종료확인','     종료할?',QMessageBox.Yes|QMessageBox.No) 
        if re == QMessageBox.Yes: 
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
    #쓰레드에서 시그널이 넘어오면 UI처리를 대신 해주는 부분 슬롯함수
    @pyqtSlot(int) #BackWorker 쓰레드에서 self, initSignal.emit() 동작해서 실행
    def initPgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal -1)

    @pyqtSlot(str)#BackWorker 쓰레드에서 self, setLog.emit() 동작해서 실행
    def setTxbLog(self, msg):
        self.txbLog.append(msg)

    @pyqtSlot(int)#BackWorker 쓰레드에서 self,setSignal.emit() 동작해서 실행
    def setpgbTask(self, val):
        self.pgbTask.setValue(val)

if __name__ == '__main__':
    loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성
    instance = qtwin_exam() # Qwidget을 상속한 qtwin_exam 객체를 생성
    instance.show()
    loop.exec_()       


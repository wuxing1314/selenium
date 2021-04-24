'''状态栏'''
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys,time

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建状态栏
        self.statusBar = self.statusBar()
        # 显示信息
        self.statusBar.showMessage('Python 3.8.5 64-bit')

        self.setGeometry(300,300,300,250)
        self.setWindowTitle('状态栏')
        self.show()

        # self.showmsg()

    def showmsg(self):
        time.sleep(2)
        self.statusBar.showMessage('转备好了...')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())
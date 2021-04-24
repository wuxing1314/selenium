'''给按钮绑定功能'''

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtCore import QCoreApplication
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建按钮
        btn = QPushButton('退出',self)
        btn.resize(btn.sizeHint())
        btn.move(100,100)
        # 给按钮绑定功能
        # btn.clicked.connect(QCoreApplication.instance().quit)
        btn.clicked.connect(self.msg)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('绑定功能')
        self.show()

    def msg(self):
        print('你好！')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())
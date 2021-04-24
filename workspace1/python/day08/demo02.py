from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys

'''
更改默认的图标样式
'''

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口大小 px: pixel
        self.setGeometry(300,300,300,200)
        # 设置窗口标题
        self.setWindowTitle('图标')
        # 设置窗口图标
        self.setWindowIcon(QIcon('python\day08\dog.png'))

        # 显示窗口
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Example()
    sys.exit(app.exec_())

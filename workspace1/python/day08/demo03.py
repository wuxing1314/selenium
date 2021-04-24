'''
实现提示语
'''

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QToolTip
from PyQt5.QtGui import QFont
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置提示信息的字体
        QToolTip.setFont(QFont('微软雅黑',10))
        # 给窗口添加一个提示
        self.setToolTip('这是<b>窗口</b>')

        # 创建一个按钮
        btn = QPushButton('按钮',self)
        # 给按钮添加提示
        btn.setToolTip('这是一个<i>按钮</i>组件')
        # 调整按钮大小
        btn.resize(btn.sizeHint())
        # 设置按钮位置
        btn.move(100,100)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('显示提示信息')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Example()
    sys.exit(app.exec_())

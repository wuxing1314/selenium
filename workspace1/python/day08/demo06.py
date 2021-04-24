'''框式布局'''

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建按钮
        okBtn = QPushButton('OK')
        cancelBtn = QPushButton('Cancel')

        # 创建水平布局方式
        hbox = QHBoxLayout()
        # 向右推动按钮
        hbox.addStretch(1)
        # 向布局中添加组件
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)

        # 创建垂直布局方式
        vbox = QVBoxLayout()
        vbox.addStretch(20)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        # 将布局方式应用到窗口中
        self.setLayout(vbox)

        self.setGeometry(300,300,300,250)
        self.setWindowTitle('框式布局')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())
    
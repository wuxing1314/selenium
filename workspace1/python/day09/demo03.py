'''菜单栏'''

from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建菜单栏
        menuBar = self.menuBar()
        # 创建菜单
        fileMenu = menuBar.addMenu('File')
        editMenu = menuBar.addMenu('Edit')
        selectionMenu = menuBar.addMenu('Selection')
        # 创建菜单项
        exitAction = QAction(QIcon('python\day09\exit3.png'),'Exit',self)
        # 添加快捷方式
        exitAction.setShortcut('Ctrl+Q')
        # 添加功能
        exitAction.triggered.connect(qApp.quit)
        # 添加到菜单中
        fileMenu.addAction(exitAction)

        self.setGeometry(300,300,300,250)
        self.setWindowTitle('菜单')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())
'''工具栏'''

from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个工具栏
        toolBar = self.addToolBar('ToolBar')
        # 添加工具
        exitAction = QAction(QIcon('python\day09\explorer.png'),'Explorer',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        editAction = QAction(QIcon('python\day09\debug.png'),'Debug',self)
        editAction.setShortcut('Ctrl+Q')
        editAction.triggered.connect(qApp.quit)

        toolBar.addAction(exitAction)
        toolBar.addAction(editAction)

        self.setGeometry(300,300,300,250)
        self.setWindowTitle('工具栏')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())
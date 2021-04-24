'''消息提示框'''

from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('消息提示框')
        self.show()

    # closeEvent()函数在关闭事件发生时自动调用
    def closeEvent(self, event):
        # 创建消息提示框
        reply = QMessageBox.question(self,'消息提示','你确定要退出吗？',QMessageBox.Yes | QMessageBox.No)
        
        # 判断用户的选择
        if reply == QMessageBox.Yes:
            event.accept() # 接受退出
        else:
            event.ignore() # 忽略        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())



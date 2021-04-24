'''pyqt5'''

from PyQt5.QtWidgets import QWidget,QApplication
import sys

app = QApplication(sys.argv)
w = QWidget()
w.show()
w.setWindowTitle('你好，PyQt5')
sys.exit(app.exec_())
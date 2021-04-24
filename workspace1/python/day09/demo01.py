'''文本编辑框'''

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QTextEdit,QGridLayout
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建标签
        title = QLabel('标题')
        author = QLabel('作者')
        content = QLabel('内容')

        # 创建文本编辑框
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()

        # 创建布局
        grid = QGridLayout()
        # 添加组件
        grid.addWidget(title,1,1)
        grid.addWidget(titleEdit,1,2)
        grid.addWidget(author,2,1)
        grid.addWidget(authorEdit,2,2)
        grid.addWidget(content,3,1)
        grid.addWidget(contentEdit,3,2)

        self.setLayout(grid)

        self.setGeometry(300,300,500,300) 
        self.setWindowTitle('文本编辑器')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())

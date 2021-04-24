'''表格布局'''

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QGridLayout
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个表格布局
        grid = QGridLayout()
        self.setLayout(grid)

        # 创建按钮的标签
        labels = ['<-','C','CE','Close',
                  '7','8','9','/',
                  '4','5','6','*',
                  '1','2','3','-',
                  '0','.','=','+'
                  ]
        
        # 创建按钮的位置
        positions = [(r,c) for r in range(5) for c in range(4)]

        # 创建按钮并添加到表格中
        for label, position in zip(labels,positions):

            btn = QPushButton(label)
            grid.addWidget(btn,*position)

        self.setWindowTitle('计算器')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())
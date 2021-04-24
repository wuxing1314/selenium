'''简单计算器'''

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QGridLayout,QLineEdit
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个表格布局
        grid = QGridLayout()
        self.setLayout(grid)

        # 创建显示窗口
        self.screen = QLineEdit()
        # 设置窗口为只读
        self.screen.setReadOnly(True)
        # 设置右对齐
        self.screen.setAlignment(Qt.AlignRight)

        grid.addWidget(self.screen,0,0,1,4)

        # 创建按钮的标签
        labels = ['<-','C','CE','Close',
                  '7','8','9','/',
                  '4','5','6','*',
                  '1','2','3','-',
                  '0','.','=','+'
                  ]
        
        # 创建按钮的位置
        positions = [(r,c) for r in range(1,6) for c in range(4)]

        # 创建按钮并添加到表格中
        for label, position in zip(labels,positions):

            btn = QPushButton(label)
            # 给按钮绑定功能
            btn.clicked.connect(self.action)
            grid.addWidget(btn,*position)

        self.setWindowTitle('计算器')
        self.show()

    # 管理者
    def action(self):
        # 获取当前被按下的按钮
        text = self.sender().text()
        if text == 'C' or text == 'CE':
            self.clear()
        elif text == 'Close':
            self.close()
        elif text == '<-':
            self.backspace()
        elif text == '=':
            self.calculate()
        else:
            self.showmsg(text)
    
    def clear(self):
        '''清空屏幕'''
        self.screen.setText('')

    def close(self):
        '''关闭计算机'''
        pass

    def backspace(self):
        '''退格'''
        self.screen.setText(self.screen.text()[:-1])

    def calculate(self):
        '''计算结果'''
        try:
            # 获取表达式
            expression = self.screen.text()
            # 计算
            result = str(eval(expression))
        except:
            result = 'err'
        finally:
            self.screen.setText(result)


    def showmsg(self,text):
        '''显示按键内容'''
        self.screen.setText(self.screen.text()+text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())
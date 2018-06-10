import sys
# 导入qt需要使用的类
from PyQt5 import QtCore,uic,QtWidgets

# 载入ui文件
form_class=uic.loadUiType("F:\\素素带你学\\python\\9-用户输入与while循环\\input\\demo.ui")[0]

# 主窗口定义
class MyWindowClass(QtWidgets.QMainWindow,form_class):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        # 给按钮绑定一个事件
        self.pushButton.clicked.connect(self.button_clicked)

    # 按钮点击事件实现
    def button_clicked(self):
        text=self.input.text()
        self.textBrowser.setText("你刚才输入了："+text)

# 显示主窗口并执行
app=QtWidgets.QApplication(sys.argv)
myWindow=MyWindowClass()
myWindow.show()
app.exec_()
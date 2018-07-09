一、PyQt使用基础
1、各种框框
Button8=QMessageBox.about(self, u'AI简介', u'AI更多知识，可以百度《一个处女座的程序猿》查看相关CSDN博客……')   #关于信息提示框
Button1_1=QMessageBox.information(self, u'对话提示信息框', u'输入的s所有信息已经存储到数据库中！', )         #对话信息提示框

Button5=QMessageBox.question(self, u'问题信息提示框', u'是否全部保存到数据库中？')                          #问题信息提示框
if Button5==0:
    print('全部保存中……')
else:
    print('没有保存') 
self.close() #关闭当前界面

Button6=QMessageBox.warning(self, u'警告信息提示框', u'没有警告信息，请继续输入！')                         #警告信息提示框
Button7=QMessageBox.critical(self, u'严重警告！', u'没有严重警告信息，请继续输入！')

my_str, ok=QInputDialog.getText(self, u'String', u'输入提示', QLineEdit.Normal, u'请在此处输入你的名字')  ##会返回两个参数(输入的信息，窗体执行状态信息)
print(my_str)

def on_pushButton_13_clicked(self):
    my_list=['Facebook', 'Google']
    my_list.append(u'阿里巴巴')
    my_list.append(u'腾讯')
    my_list.append(u'百度')
    my_str, ok=QInputDialog.getItem(self, u'Dropdown box',u'请选择你想进入的公司', my_list )
    self.textBrowser.append('COMPANY'+':'+my_str) #向多行文本添加内容



2、常用控件
self.radioButton_12.setChecked(True)   #该radioButton_12按钮被选中
webbrowser.open('www.baidu.com')       #默认浏览器打开指定网址
self.graphicsView.setStyleSheet("border-image: url(:/im/image/AI (4).jpg);")   #采用graphicsView控件显示图片
self.label_4.setStyleSheet("border-image: url(:/im/image/Bigdata.jpg);")       #采用label_4标签显示图片

def on_dial_valueChanged(self, value):   #lcdNumber控件显示数值
    self.lcdNumber.display(value)
    print(value)
def on_horizontalSlider_valueChanged(self, value):
    self.lcdNumber.display(value)
    

3、控件及其属性
my_str=self.lineEdit.text()             #获取单行文本框的内容
word =self.textEdit.toPlainText()   #获取textEdit多行文本框的内容
my_str=self.textBrowser.toPlainText()   #获取textBrowser控件文本框的内容


str01="输出信息！"
print(str01)
self.textEdit_3.append(str01)      #向textEdit_3控件添加文本内容

result1="输出信息！"
self.textBrowser.append(result1)   #向textBrowser控件多行文本框添加文本内容


self.lineEdit.setText( "")  #清除单行文本框lineEdit内容
self.textEdit_3.setText("") #清除多行文本框textEdit_3内容


4、GUI常用函数
sys.exit(0) #退出系统



5、GUI常用其他

spk.Speak(u"欢迎访问我的CSDN博客，谢谢！") 


二、经典案例(仅限代长代码案例)
PyQt5：PyQt5常用控件、函数、简单案例总结
https://blog.csdn.net/qq_41185868/article/details/80457932
PyQt之GUI界面：基于QtGUI界面编程的控件简介、槽函数使用详细攻略
https://blog.csdn.net/qq_41185868/article/details/80426721
1、




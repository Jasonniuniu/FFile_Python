相关文章
PyQt5：PyQt5常用控件、属性、函数、简单案例总结
https://blog.csdn.net/qq_41185868/article/details/80457932


一、PyQt使用基础
1、各种框框
from PyQt5.QtWidgets import QMessageBox 

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
self.label_4.setScaledContents (True)  #使图片调整为label大小

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

PyQT界面上显示动态GIF图片
self.movie01 = QtGui.QMovie("Resources/robot.gif") 
self.movie01.setCacheMode(QtGui.QMovie.CacheAll)    #CacheNone #设置cacheMode为CacheAll时表示gif无限循环，注意此时loopCount()返回-1      
self.movie01.setSpeed(100)            #播放速度
self.label_26.setMovie(self.movie01)  #self.movie_screen是在qt designer里定义的一个QLabel对象的对象名，将gif显示在label上
self.movie01.start()                  #开始播放，对应的是movie.start() 
#movie.stop() #停止图片显示

Label上显示本地图片
T1、加载定义好的图片
self.graphicsView.setStyleSheet("border-image: url(:/im/image/AI (4).jpg);")   #显示图片或更改图片
self.label_26.setPixmap (QPixmap ("Resources/BigD (1).jpg"))   # 在label上显示图片
self.label_26.setScaledContents (True)  # 让图片自适应label大小
self.label_26.setPixmap(QPixmap(""))       #移除label上的图片
T2、加载新生成的图片
from PyQt5.QtGui import QPixmap
self.label.setPixmap (QPixmap ('QR.png'))
self.label.setScaledContents (True)  #使图片调整为label大小


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





三、其他长案例
1、Python多线程实例：采用自定义一个类，继承该模块，重写run的方法
import threading
# import queue as Queue
from time import sleep, ctime

class MyThread(threading.Thread):  #自定义多线程的类
    def __init__(seLf, func, args, name=''): #对类进行初始化
        threading.Thread.__init__(seLf)  
        seLf .name=name                  #传递三个参数
        seLf.func=func
        seLf.args=args 
        
        self.thread_flag=0  #线程初始标记为0
        self.start_flag=1
        
    def getresult(seLf):  #获得结果
        return self.res
        
    def run(self):        #重写run方法
        print ('staring', self.name, 'at:', ctime())  #标记类运行初始时间
        self.res=self.func(self.args)   #python2中的用法，apply(self.func, self.args)
        print( self.name, 'finished at:', ctime())   #标记类运行结束时间

#(1)、主窗口中还要继承这个threading.Thread类：
#(2)、然后初始化父类
#(3)、定义run方法
#(4)、主方法中开启线程，即调用threading.Thread的start方法即可
#class MainWindow(QMainWindow, Ui_MainWindow)  1、主窗口中还要继承这个threading.Thread类：
class MainWindow(QMainWindow, Ui_MainWindow, threading.Thread):  
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        threading.Thread.__init__(self)       #2、然后初始化父类

    def run(self):  #3、定义run方法
        print ('staring', self.name, 'at:', ctime())  
        self.res=self.my_record()  #self.func换为需要多线程的函数，比如my_record()让录音先一直运行
        #self.res=self.my_record(*self.args)     #需要传递参数时的用法，python3中
        print( self.name, 'finished at:', ctime())
    def audio2txt(self, token):   #get_word(token)
        pass
    
    @pyqtSlot()
    def on_pushButton_20_clicked(self):
        
        #设计第二个线程：通过点击按钮20启动，点击按钮19结束线程
        if self.thread_flag==0:  #如果没有开启线程，就
            self.start_flag=1    #线程标记开始
            
            #识别程序在上边的主类中实现(且一直在识别)，而这个线程开启的是录音
            record_t=MyThread(self.my_record, (self,), self.my_record.__name__)  #开启线录音线程，record_t=MyThread(开启线程的函数, 传递的第一个参数, ui.audio2txt.__name__)
            record_t.setDaemon(True)#进程随之结束
            record_t.start()    #进程随之结束
            self.thread_flag=1  #标记为1，为本线程结束做标记，目的是通知其他线程可以开启
            
    @pyqtSlot()
    def on_pushButton_19_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.thread_flag==1:  #如果得到信息通知，线程开启,，就关闭掉，将其他标记变量归零
            self.start_flag=0    #标记变量归零
            self.thread_flag=0   #线程标记变量归零

if __name__ == "__main__":  
    ui = MainWindow() 
    
    #设计第一个线程
    ui.setDaemon(True)  #线程开启之前设置属性。因为ui.start()是子线程，我们要让这个子线程，随着父线程结束而结束
    ui.start()          #开启线程(此时self.my_record()函数会起作用)。因Ui已继承threading.Thread，故可直接调用线程thread中的start方法。
    #self.my_record()函数会一直运行，直到等父线程结束才结束
    
    ui.show()  
        

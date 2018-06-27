#传入一个文件路径，返回文件的内容
import docx
def niu_read_docx(filename):
     doc=docx.Document(filename)
     fulltext=[]
     for para in doc.paragraphs:
         fulltext.append(para.text)
     return '\n'.join(fulltext)
self.textBrowser.append(niu_read_docx(my_file_path)) #添加到显示的多行文本控件上

#局部变量变为全局变量的方法
改变之前
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        my_dir=QFileDialog.getExistingDirectory(self, '选择文件夹', '/')  #Pyqt提供标准的选择文件夹对话框
        print(my_dir)
改变之后
  class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    my_dir=''  #将局部变量声明为全局变量，先初始化，再self.my_dir
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
     
#对输出的文字加一个个蹦出特效：类似在电影字幕中的字母会一个一个的蹦出来，即将dramaticTyping函数代替print函数
import time
import sys

def dramaticTyping(string):
    for char in string:
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(0.04)

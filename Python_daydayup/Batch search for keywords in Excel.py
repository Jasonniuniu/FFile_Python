# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_Search import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog 

from glob import glob
from os.path import join

import os
import re


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
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.my_dir=QFileDialog.getExistingDirectory(self, '选择文件夹', '/')  #Pyqt提供标准的选择文件夹对话框
        print(self.my_dir)
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        print(self.my_dir)
        #T1、采用glob模块一句话进行匹配搜查
        result=glob(join(self.my_dir, '*.xlsx'))  #可以匹配png、jpg、txt等文件。将该文件夹下的文件路径全部打印出来
        #输出的是一个列表，如F:/File_Python/Python_GUI/Batch search for keywords in Excel/test\\test01.xlsx
        print(result)
        
        #T2、采用os模块两句话进行匹配搜查
        print(os.path.isdir(self.my_dir))
        if os.path.isdir(self.my_dir):  #判断是不是一个文件夹
            print(os.listdir(self.my_dir)) #将该文件夹下的文件全部打印出来，而不是文件路径
            #输出的是一个列表，如'doc01.docx', 'doc02.docx', 'test01.xlsx', 
            
        #T3、glob模式匹配结合excel搜索
        lineEdit=self.lineEdit.text()
        print('text is :', lineEdit)
        my_list=re.split(' ',lineEdit)  #去掉输入的空格
        print(my_list)
#        for eachone in my_list:  
#            print(eachone) #从列表中依次单个输出，即用户的关键词
        
        for fn in glob(join(self.my_dir, '*.xlsx')) :
            print(fn)  #输出搜索到的每个xlsx文件所在路径
            from xlrd import open_workbook
            wb=open_workbook(fn.replace(u'/', u'\\'))
            print(wb)
            for s in wb.sheets():
                for row in range(s.nrows):  
                    for col in range(s.ncols):
                        if s.cell(row, col).value:    #if条件判断空格为1才去输出，(0即空格则不输出)
                            print(s.cell(row, col).value)
                            for eachone in my_list:  
                                if eachone in s.cell(row, col).value:  #如果文本内容中含有用户输入的关键词
                                    print('Yeah,find it!')
                                    self.textBrowser.append(fn.replace(u'/', u'\\')) #如果匹配到关键词就加到多行文本控件中
                                    
        
    @pyqtSlot()
    def on_actionOpen_triggered(self):
        """
        Slot documentation goes here.
        """
    
    @pyqtSlot()
    def on_actionOpen_2_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionSave_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionClose_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionClose_2_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionClose_3_triggered(self):
        """
        Slot documentation goes here.
        """
        sys.exit(0) #退出
    
    @pyqtSlot()
    def on_actionCopy_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionPaste_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionCut_3_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionUndo_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionRedo_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionDelete_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionSelect_All_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionAbout_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionRegister_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionOfficial_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionContact_Us_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
        
        
        
if __name__ == "__main__":  
    import sys  
    app = QtWidgets.QApplication(sys.argv)  
    ui = MainWindow()  
    ui.show()  
    sys.exit(app.exec_())
   

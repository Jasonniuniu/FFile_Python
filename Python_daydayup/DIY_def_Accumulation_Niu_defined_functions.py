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
  


#对列表取值生成统计图的两个函数
def list_count(list): #实现根据输入的列表，统计列表各元素个数生成字典，并返回字典的Keys,Values
    list_dict = {}
    for i in list:  #计算列表每个元素的个数并生成字典
        if list.count(i) >= 0:
            list_dict[i] = list.count(i)
    print(list_dict)
    keys=list_dict.keys()
    
    #for循环遍历字典分别取出keys、values各组成列表
    Keys=[]
    Values=[]
    for key in list_dict.keys(): #for循环遍历字典的keys、values
    #     print(key)
        Keys.append(key)
    for value in list_dict.values():
    #     print(value)
        Values.append(value)   
    print(Keys)
    print(Values)
    return Keys,Values
def draw(Keys,Values,title,xlabel,ylabel):  #实现根据输入的Keys,Values生成相应的柱状图、圆饼图
    import matplotlib.pyplot as plt
    import numpy as np  
    import matplotlib.mlab as mlab  
    
    #绘制柱状图
    X=Keys
    Y=Values 
    fig = plt.figure()
    plt.rcParams['font.sans-serif']=['SimHei']  #手动添加中文字体，
    
    plt.bar(X,Y,0.5,color="green")  #0.5是指柱状的宽度比例
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    plt.title(title)
    plt.show()  
    
    #绘制圆饼图
    #explode=[0,0.1,0,0]   #逆时针顺序，第几个分离
    explode_list=[0]*(len(Keys)-1)
    explode_list.append(0.1)
    print(explode_list)
    colors='yellowgreen','gold','lightskyblue','lightcoral'
    
    plt.pie(Values,explode=explode_list,labels=Keys,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
    plt.axis('equal')
    plt.title(title)
    plt.show()   
list=['America', 'America', '山东', '山东', '吉林', '山东', '上海', '上海']
print(list.count("山东")) #计算列表指定元素的个数
Keys,Values=list_count(list)
title="现场人员地区分布个数——Jason Niu"
xlabel="地区分布"
ylabel="人数统计"
draw(Keys,Values,title,xlabel,ylabel)



#类3D绘图：2Dbar graphs in different planes
def twoD_in_different_planes(xs,ys,Xlabel,Ylabel,Zlabel,title):
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np
    
    np.random.seed() #19680801 Fixing random state for reproducibility
    
    fig = plt.figure()
    plt.rcParams['font.sans-serif']=['SimHei']  #手动添加中文字体，
    ax = fig.add_subplot(111, projection='3d')
    
    colors = ['r', 'g', 'b', 'y']
    yticks = [3, 2, 1, 0]
    for c, k in zip(colors, yticks):
        # Generate the random data for the y=k 'layer'.
#         xs01 = np.arange(20)
#         ys01 = np.random.rand(20)

        # You can provide either a single color or an array with the same length as
        # xs and ys. To demonstrate this, we color the first bar of each set cyan.
        cs = [c] * len(xs)
        cs[0] = 'c'
    
        # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
        ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)
    ax.set_xlabel(Xlabel)
    ax.set_ylabel(Ylabel)
    ax.set_zlabel(Zlabel)

    # On the y axis let's only label the discrete values that we have data for.
    ax.set_yticks(yticks)
    plt.title(title)
    plt.show()  
xs=['AndrewNg', 'Elon Musk', 'Jason Niu', '牛魔王', '李笑来', '胡歌', '江疏影']
ys=[1, 1, 1, 2, 1, 1, 1]
Xlabel="Name"
Ylabel="Different layers"
Zlabel="Statistical number"

title="2Dbar graphs in different planes"
twoD_in_different_planes(xs,ys,Xlabel,Ylabel,Zlabel,title)


#查找names列表中的重复元,只输出有重复的元素、及其重复元素对应不同的索引值
def list_dup(names):
    from collections import defaultdict
    def list_dup_nameAndindexs(names):
        tally = defaultdict(list)  #defaultdict类就好像是一个dict，但是它是使用一个类型来初始化的
        for i,item in enumerate(names):
            tally[item].append(i) 
        return ( (key,locs) for key,locs in tally.items() if len(locs)>1 )
    dup_list=sorted(list_dup_nameAndindexs(addresss)) 
    #print(dup_list)
    
    #for循环获取list_dup_nameAndindexs中的name并存为一个列表
    dup_names=[]
    for a in dup_list:
        dup_names.append(a[0])
    #print(dup_names)
    return dup_names,dup_list

addresss=['汕头', '杭州', '周口', '广元', '佛山', '佛山', '上海', '宁波', '东莞', '台州', '仙桃', '阳泉', '安庆', '泉州', '黄冈', '宿迁', '黄冈', '常州', '杭州', '潮州', '东阳', '淮安', '重庆', '廊坊', '威海', '黄石', '北京', '成都', '保定', '上海', '佛山', '绍兴']
dup_names,dup_list=list_dup(addresss)
print(dup_names,dup_list)
['上海', '佛山', '杭州', '黄冈'] [('上海', [6, 29]), ('佛山', [4, 5, 30]), ('杭州', [1, 18]), ('黄冈', [14, 16])]


#将excel表格的内容取出并存在一个列表内，返回的list是表格所有的内容，返回的list0是指第j列所有的内容
def xls2list(data_pat,sheetnam,j):
    import xlrd       
    xls1 = xlrd.open_workbook(data_pat)
    table = xls1.sheet_by_name(sheetnam)
    #第一个for循环取出表格内文件存为list01列表中
    list = [] 
    list0 = [] 
    for i in range(0,table.nrows):                                  #table.nrows输出表格的行数
        list.append(table.row_values(i))
        list0.append(table.row_values(i)[j])
    return list,list0

data_pat="map/AI.xlsx"
data_path='map/The latitude and longitude tables of Chinese cities.xls'
sheetname='Sheet1'
j=1
list,list0=xls2list(data_path,sheetname,j)

print(list) 
print(list0) 
print(list0[1:])  #获取除了第一列的内容(除了第一行(列名) 以外的所有行的内容)




#调用默认浏览器自动循环打开网页
import webbrowser as web    
import time    
import os    
import random    
count = random.randint(1,2)    
j=0    
while j<count:    
    i=0    
    while i<=8 :    
        web.open_new_tab('https://blog.csdn.net/qq_41185868/article/details/80396490')  #网址替换这里  
        i=i+1    
        time.sleep(3)  #这个时间根据自己电脑处理速度设置，单位是s  
    else:    
        time.sleep(10)  
#         <span style="font-family: Arial, Helvetica, sans-serif;">#这个时间根据自己电脑处理速度设置，单位是s</span>  
        os.system('taskkill /F /IM chrome.exe')  #google浏览器，其他的更换下就行  
        #print 'time webbrower closed'  
          
    j=j+1    
time.sleep(15)

#基于python实现后台增加网页浏览量(better)
import urllib    # Python中的cURL库    
import requests
import time    # 时间函数库，包含休眠函数sleep()    
url = 'https://blog.csdn.net/qq_41185868/article/details/80396490'    # 希望刷阅读量的文章的URL    
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'    # 伪装成Chrome浏览器    
refererData = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=monline_3_dg&wd=python%20%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E7%BB%83%E4%B9%A0&oq=urllib2.request%20%E5%8F%82%E6%95%B0&rsv_pq=fd0f38e40000db8b&rsv_t=6ec2HIbgWthuw3DWeXZSp8H8sFOXlNADvNuj1cCIHdsA6JxxgKiMJ3EWA1cwZTGowTpL&rqlang=cn&rsv_enter=0&inputT=18403&rsv_sug3=131&rsv_sug1=70&rsv_sug7=101&rsv_sug4=19841'    # 伪装成是从baidu.com搜索到的文章    
data = ''    # 将GET方法中待发送的数据设置为空    
headers = {'User-Agent' : user_agent, 'Referer' : refererData}    # 构造GET方法中的Header    
count = 0    # 初始化计数器    
request = urllib2.Request(url, data, headers)    # 组装GET方法的请求    
while 1:    # 一旦开刷就停不下来      
    rec = urllib.request.urlopen(url)   # 发送GET请求，获取博客文章页面资源    
    page = rec.read()    # 读取页面内容到内存中的变量，这句代码可以不要    
    count += 1    # 计数器加1    
    print ('当前正在进行第'+str(count)+'次网页阅读！')    # 打印当前循环次数    
    if count % 6:    # 每6次访问为1个循环，其中5次访问等待时间为31秒，另1次为61秒    
        time.sleep(31)    # 为每次页面访问设置等待时间是必须的，过于频繁的访问会让服务器发现刷阅读量的猥琐行为并停止累计阅读次数    
    else:    
        time.sleep(61)    
print (page)    # 打印页面信息，这句代码永远不会执行 

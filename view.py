# coding utf-8

from tkinter import *
from tkinter.tix import Tk, Control, ComboBox  #升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import threading
import os
import json

# 开始
def start():
    global isStart
    isStart = True
    name = entryName.get()
    nameArr = handleStr(name)
    threadIt(beginClick, nameArr)
    
# 处理字符串
def handleStr(strs):
    strs = str(strs)
    strArr = strs.split(',')
    returnArr = []
    for i in strArr:
        _i = i.strip()
        if _i == '':
            continue
        returnArr.append(i)
    return returnArr

# 开始执行
def beginClick(arr):
    # 开始模拟点击
    for i in arr :
        threadIt(autoClick, i)
        
# 开启线程
def threadIt(func, *args):
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护线程
    t.setDaemon(True)
    # 启动线程
    t.start()

# 自动点击
def autoClick(i):
    global isStart
    global browser
    while isStart:
        try:
            print('正在点击'+i)
            browser.find_element_by_link_text(i).click()
        except:
            print(i+"按钮不存在")

# 打开链接
def openLink():
    global browser
    link = entryLink.get()
    if browser == False :
        browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=chrome_options)
    try:
        browser.get(link)
    except:
        link = link.lstrip()
        if link[0:3] != 'http':
            threadIt(popDiv, 1, '提示', 'url使用http或https协议头')
            link = 'http://' + link
        browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=chrome_options)
        browser.get(link)

def popDiv(type, title, content):
    type = int(type)
    if type == 1:
        re = showinfo(title, content)
    elif type == 2:
        re = showwarning(title, content)
    elif type == 3:
        re = showerror(title, content)
    else :
        re = False
    return re

# 结束
def pause():
    global isStart
    isStart = False

# -----------文件menu操作-------------
# 保存配置
def save():
    link = entryLink.get()
    name = entryName.get()
    children = Toplevel()
    children.title('保存配置')
    
    children.geometry("300x200")
    children.resizable(width=False, height=False)
    
    labelLink = Label(children, text="网址:"+link, font=("Microsoft YaHei",12), height=3, anchor=W, wraplength = 280, justify = 'left')
    labelLink.grid(row = 0)

    labelName = Label(children, text="按钮:"+name, font=("Microsoft YaHei",12), height=3, anchor=W, wraplength = 280, justify = 'left')
    labelName.grid(row = 1)

    entrySaveName = Entry(children, font=("Microsoft YaHei",12), width=15)
    entrySaveName.grid(row = 2, column = 1)

    buttonSave = Button(children, 
                        text='保存', 
                        padx=20, 
                        command=lambda:saveFile())  
    buttonSave.grid(row=2)

def saveFile():
    path = './save.log'
    res = os.access(path, os.F_OK)
    if res == False:
        try:
            f = open(path, "w+")
            data = f.read()
            data = json.loads(data)

        except:
            popDiv(2, '写入警告', '文件写入失败')
    
# -----------------------------------


# ------------------- 浏览器服务设置----------------------
chromedriver = "C:\\Users\\sgm\\Desktop\\sgm\\autoOrderTMall\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
# -------------------------------------------------------

isStart = False
browser = False

root = Tk(); #初始化tk
root.title("create by sgm")    # 设置窗口标题
root.geometry("400x230")    # 设置窗口大小
root.resizable(width=False, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
# root.tk.eval('package require Tix')  #引入升级包，这样才能使用升级的组合控件

# 提示
labelLink = Label(root, text="网址:", font=("Microsoft YaHei",12), width=8, height=3, anchor=W)
labelLink.grid(row = 0)
# 输入框
entryLink = Entry(root, font=("Microsoft YaHei",12), width=25)
entryLink.grid(row = 0, column = 1)

buttonOpenLink=Button(root,
              text='打开链接',
              command=lambda:threadIt(openLink),
              padx=20)
buttonOpenLink.grid(row = 1)

labelName = Label(root, text="需要点击的按钮:", font=("Microsoft YaHei",12), width=15, height=3)
labelName.grid(row = 2)

entryName = Entry(root, font=("Microsoft YaHei",12), width=25)
entryName.grid(row = 2, column = 1)

buttonStart=Button(root,
              text='开始',
              command=lambda:start(),
              padx=20)
buttonStart.grid(row = 3)

buttonEnd=Button(root,
              text='结束',
              command=pause,
              padx=20)
buttonEnd.grid(row = 3, column = 1)


menubar=Menu(root)
root.config(menu=menubar)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='文件',menu=filemenu)
filemenu.add_command(label='加载',command=lambda:loading())
filemenu.add_command(label='保存',command=lambda:save())

root.mainloop()
# -*- coding: utf-8 -*
#####################################################################################
# k-means算法GUI绘制程序
# python 2.7
# author:胡子涵
# 2018/11/21
#####################################################################################

# 导入Tkinter绘制GUI
from Tkinter import *
import Tkinter as tk
import tkFileDialog
import os
# 导入k-means算法实现
import k_means as km


# 绘制GUI窗口
class Application(Frame):
    # k-means算法k值
    k = 2
    # 导入的文件路径(.csv文件)
    filePath = ""
    # k-means距离计算方式
    distanceType = ""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.filePath = ""
        self.pack()
        self.createWidgets()
        self.k = 2


    # 从文件对话框导入文件
    def OpenFile(self,Lable_filePath):
        default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
        self.filePath = tkFileDialog.askopenfilename(title=u"选择文件", initialdir=(os.path.expanduser(default_dir)))
        Lable_filePath.config(text=("文件: "+str(self.filePath))) # 更新界面中的文件路径显示

    # 运行k-means算法进行聚类分析
    def Start(self):
        km.k_means(self.filePath,self.k,self.distanceType)

    # 增加k值
    def addK(self,Label_k):
        self.k = self.k + 1
        Label_k.config(text=("K值："+str(self.k))) # 更新界面中的k值显示

    # 减小k值
    def decK(self,Label_k):
        self.k = self.k -  1
        Label_k.config(text=("K值："+str(self.k))) # 更新界面中的k值显示

    # 设置k-means算法距离计算方式
    def selectDistType(self,distType):
        self.distanceType = distType

    # 创建widgets，绘制GUI控件
    def createWidgets(self):
        # Label
        Label_titile = tk.Label(root, text='K-means算法演示程序')
        Label_titile.place(x=200, y=20, anchor="center")

        Label_author = tk.Label(root, text='作者:胡子涵')
        Label_author.place(x=150, y=180)

        Lable_filePath = tk.Label(root, text=("文件: "+str(self.filePath)))
        Lable_filePath.place(x=260, y=100)

        Label_k = tk.Label(root, text=("K值："+str(self.k)))
        Label_k.place(x=190, y=50)

        # Button
        Button_openFile = tk.Button(root, text="导入数据", command=lambda:self.OpenFile(Lable_filePath))
        Button_openFile.place(x=50, y=100)

        Button_start = tk.Button(root, text="开始程序", command=self.Start)
        Button_start.place(x=120, y=100)

        Button_exit = tk.Button(root, text="关闭", command=root.quit)
        Button_exit.place(x=190, y=100)

        Button_addK = tk.Button(root, text="增加", command=lambda:self.addK(Label_k))
        Button_addK.place(x=50, y=50)

        Button_decK = tk.Button(root, text="减小", command=lambda:self.decK(Label_k))
        Button_decK.place(x=120, y=50)


        # OptionMenu
        distType = StringVar(root)
        distType.set("欧氏距离")  # default value
        distTypeMenu = OptionMenu(root, distType, "欧氏距离", "曼哈顿距离", "闵可夫斯基距离",command=self.selectDistType)
        distTypeMenu.place(x=260,y=50)


if __name__=="__main__":
    root = tk.Tk()
    root.geometry("400x200+10+10")
    root.title("K-means算法演示程序")
    app = Application(master=root)
    root.mainloop()


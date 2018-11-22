# -*- coding: utf-8 -*
####################################################################################
# 使用matplotlib画图显示聚类结果
# python 2.7
# author:胡子涵
# 2018/11/21
#####################################################################################

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
#加载PCA算法包，用于对多维数据降维至二维，方便可视化
from sklearn.datasets import load_iris

# 绘图颜色表
colorDic = {0: 'aliceblue'  , 1: 'antiquewhite', 2: 'aqua'           , 3: 'aquamarine'    , 4: 'azure',\
            5: 'beige'      , 6: 'bisque'      , 7: 'black'          , 8: 'blanchedalmond', 9: 'blue' ,\
            10: 'blueviolet', 11: 'brown'      , 12: 'burlywood'     , 13: 'cadetblue'    , 14: 'chartreuse',\
            15: 'chocolate' , 16: 'coral'      , 17: 'cornflowerblue', 18: 'cornsilk'     , 19: 'crimson'}


# 初始化数据，将传入的dataSet数据去除分类标记，用于之后进行降维
def initData(dataSet):
    newDataSet = []
    for i in range(0,len(dataSet)):
        newDataSet.append(dataSet[i][0])
    return newDataSet

# 使用PCA算法对多维数据进行降维操作，降至二维
def DimensionalityReduction(dataSet):
    pca = PCA(n_components=2)
    # 加载PCA算法，设置降维后主成分数目为2
    dataRedu = pca.fit_transform(dataSet)
    # 对原始数据进行降维，保存在reduced_X中
    return dataRedu

# 画图显示聚类结果
def show(dataSet,center):
    newDataSet = initData(dataSet)
    tmpData = DimensionalityReduction(newDataSet+center)
    dataRedu = tmpData[0:(len(tmpData)-len(center))]
    centerRedu = tmpData[len(newDataSet):(len(tmpData))]

    # 将数据按照类别分类保存至classify
    classify = {}

    # 逐类数据画图
    for i in range(0,len(center)):
        tmpx = []
        tmpy = []
        for j in range(0,len(dataSet)):

            if dataSet[j][1] == center[i]:
                tmpx.append(dataRedu[j][0])
                tmpy.append(dataRedu[j][1])
        plt.scatter(tmpx, tmpy, c=colorDic[16 - i], marker='.', s=30) # 数据点
        plt.scatter(centerRedu[i][0], centerRedu[i][1], c=colorDic[16 - i], marker='^', s=40) # 聚类中心点

    plt.show()
# -*- coding: utf-8 -*
####################################################################################
# k-means算法实现
# python 2.7
# author:胡子涵
# 2018/11/21
#####################################################################################
#   k_means算法流程
# 1 从D中随机取k个元素，作为k个簇的各自的中心。
# 2 分别计算剩下的元素到k个簇中心的相异度，将这些元素分别划归到相异度最低的簇。
# 3 根据聚类结果，重新计算k个簇各自的中心，计算方法是取簇中所有元素各自维度的算术平均数。
# 4 将D中全部元素按照新的中心重新聚类。
# 5 重复第4步，直到聚类结果不再变化。
# 6 将结果输出。
#####################################################################################
from math import sqrt
# 导入show模块，用于绘制结果
import show as sh


# 读取数据文件到data数据集中
def loadFile(filePath):
    dataSet = []
    with open(filePath,"r") as file:
        for line in file:
            dataSet.append([list(map(float, line.split(','))),None])
        return dataSet

# 计算两点之间的距离
def distance(data1,data2,distanchType):
    # 根据传入的距离计算类型选择计算方法
    if(distanchType == "欧拉距离"):
        return eulerDist(dataSet,k) # 欧拉距离
    elif(distanchType == "曼哈顿距离"):
        return manhattanDist(data1,data2) # 曼哈顿距离
    else:
        return chebyshevDist(data1,data2) # 切比雪夫距离

# 欧拉距离
def eulerDist(data1,data2):
    size = len(data1)
    tmp = 0
    for i in range(0, size):
        tmp += pow(data1[i] - data2[i], 2)
    return sqrt(tmp)

# 曼哈顿距离
def manhattanDist(data1,data2):
    size = len(data1)
    tmp = 0
    for i in range(0, size):
        tmp += abs(data1[i] - data2[i])
    return tmp

# 切比雪夫距离
def chebyshevDist(data1,data2):
    size = len(data1)
    tmp = []
    for i in range(0, size):
        tmp.append(abs(data1[i] - data2[i]))
    return max(tmp)


# 初始化k个聚类中心
def initCenter(dataSet,k):
    center = []
    for i in range(0,k):
        center.append(dataSet[i][0])
    return center

# 聚类,将各个数据划分到对应的聚类中心
def clusting(center,dataSet,k,distanchType):
    for data in dataSet:
        dist = []
        for i in range(0,k):
            dist.append(distance(center[i],data[0],distanchType))
        data[1] = center[dist.index(min(dist))]

# 更新聚类中心
def resetCenter(center,dataSet,k):
    for i in range(0,k):
        index = [j for j in range(0,len(dataSet)) if dataSet[j][1] == center[i]]
        tmp = []
        for j in range(0,len(center[0])):
            tmp.append(0)

        for j in index:
            for k in range(len(center[0])):
                tmp[k]=tmp[k] + dataSet[j][0][k]
        center[i] = [x/len(index) for x in tmp]
    return center


# k-means算法主程序
def k_means(filePath,k,distanchType):
    dataSet = loadFile(filePath)
    center = initCenter(dataSet,k)
    clusting(center,dataSet,k,distanchType)
    centerPre = center
    center = resetCenter(center,dataSet,k)

    # 当聚类中心不再改变则停止算法
    while(centerPre != center):
        clusting(center, dataSet, k,distanchType)
        centerPre = center
        center = resetCenter()
    clusting(center, dataSet, k,distanchType)

    # 画图显示聚类结果
    print center
    sh.show(dataSet, center)


# k-means算法

[TOC]



## 1. k-means算法简介 

k-means算法是一种聚类算法，所谓聚类，即根据相似性原则，将具有较高相似度的数据对象划分至同一类簇，将具有较高相异度的数据对象划分至不同类簇。聚类与分类最大的区别在于，聚类过程为无监督过程，即待处理数据对象没有任何先验知识，而分类过程为有监督过程，即存在有先验知识的训练数据集。 

k-means算法中的k代表类簇个数，means代表类簇内数据对象的均值（这种均值是一种对类簇中心的描述），因此，k-means算法又称为k-均值算法。k-means算法是一种基于划分的聚类算法，以距离作为数据对象间相似性度量的标准，即数据对象间的距离越小，则它们的相似性越高，则它们越有可能在同一个类簇。数据对象间距离的计算有很多种，k-means算法通常采用欧氏距离来计算数据对象间的距离。

## 2.k-means算法详解 
k-means算法以距离作为数据对象间相似性度量的标准，通常采用欧氏距离来计算数据对象间的距离。K-Means的算法如下：

1 从D中随机取k个元素，作为k个簇的各自的中心。
2 分别计算剩下的元素到k个簇中心的相异度，将这些元素分别划归到相异度最低的簇。
3 根据聚类结果，重新计算k个簇各自的中心，计算方法是取簇中所有元素各自维度的算术平均数。
4 将D中全部元素按照新的中心重新聚类。
5 重复第4步，直到聚类结果不再变化。
6 将结果输出。

## 3.求点群中心的算法

聚类分析有以下几个常用的计算聚类公式：

**1）Minkowski Distance 公式 ——** λ 可以随意取值，可以是负数，也可以是正数，或是无穷大。

![Minkowski Distance 公式](https://coolshell.cn/wp-content/uploads/2012/06/MinkowskiDistance_clip_image102.gif)

**2）Euclidean Distance 公式** —— 也就是第一个公式 λ=2 的情况

![Euclidean Distance 公式](https://coolshell.cn/wp-content/uploads/2012/06/EuclideanDistance_clip_image002.gif)

**3）CityBlock Distance 公式** —— 也就是第一个公式 λ=1 的情况

![CityBlock Distance 公式](https://coolshell.cn/wp-content/uploads/2012/06/CityBlockDistance_clip_image002.gif)

## 4.K-Means算法分析

K-Means主要有两个最重大的缺陷——都和初始值有关：

-  K 是事先给定的，这个 K 值的选定是非常难以估计的。很多时候，事先并不知道给定的数据集应该分成多少个类别才最合适。

- K-Means算法的初始聚类中心时随机的，不同的随机结果会有得到完全不同的结果。
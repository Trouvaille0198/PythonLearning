from __future__ import print_function
import numpy as np
import pandas as pd
# import random

# from sklearn.mixture import GaussianMixture
# model = GaussianMixture(n_components=n_clusters, init_params='kmeans')
# model.fit(X)
# print(model.aic(X))

##
# 通过设定超参数K同时考虑行程耗时与平均值和协方差

# x = []
# y = []
# random.choice(x)
# ##随机选取一个
# random.sample(x,2)
# #随机选取n个
#
#
# dist1 = np.linalg.norm(x - y)
# 欧氏距离公式计算
# x,y代表不同的对象
# 通过使用AICc赤道信息准则评估模型
# 计算AIC(k: number of variables, n: number of observations)
# def AIC(y_test, y_pred, k, n):
#     resid = y_test - y_pred
#     SSR = sum(resid ** 2)
#     AICValue = 2*k+n*log(float(SSR)/n)
#     return AICValue


def generateData(k, mu, sigma, dataNum):
    '''
    产生混合高斯模型的数据
    :param k: 比例系数
    :param mu: 均值
    :param sigma: 标准差
    :param dataNum:数据个数
    :return: 生成的数据
    '''
    # 初始化数据
    dataArray = np.zeros(dataNum, dtype=np.float32)
    # 逐个依据概率产生数据
    # 高斯分布个数
    n = len(k)
    for i in range(dataNum):
        # 产生[0,1]之间的随机数
        rand = np.random.random()
        Sum = 0
        index = 0
        while (index < n):
            Sum += k[index]
            if (rand < Sum):
                dataArray[i] = np.random.normal(mu[index], sigma[index])
                break
            else:
                index += 1
    return dataArray


def normPdf(x, mu, sigma):
    '''
    计算均值为mu，标准差为sigma的正态分布函数的密度函数值
    :param x: x值
    :param mu: 均值
    :param sigma: 标准差
    :return: x处的密度函数值
    '''
    return (1. / np.sqrt(2 * np.pi)) * (np.exp(-(x - mu)**2 / (2 * sigma**2)))


def em(dataArray, k, mu, sigma, step=10):
    '''
    em算法估计高斯混合模型
    :param dataNum: 已知数据个数
    :param k: 每个高斯分布的估计系数
    :param mu: 每个高斯分布的估计均值
    :param sigma: 每个高斯分布的估计标准差
    :param step:迭代次数
    :return: em 估计迭代结束估计的参数值[k,mu,sigma]
    '''
    # 高斯分布个数
    n = len(k)
    # 数据个数
    dataNum = dataArray.size
    # 初始化gama数组
    gamaArray = np.zeros((n, dataNum))
    for s in range(step):
        for i in range(n):
            for j in range(dataNum):
                Sum = sum([
                    k[t] * normPdf(dataArray[j], mu[t], sigma[t])
                    for t in range(n)
                ])
                gamaArray[i][j] = k[i] * \
                    normPdf(dataArray[j], mu[i], sigma[i]) / float(Sum)
        # 更新 mu
        for i in range(n):
            mu[i] = np.sum(gamaArray[i] * dataArray) / np.sum(gamaArray[i])
        # 更新 sigma
        for i in range(n):
            sigma[i] = np.sqrt(
                np.sum(gamaArray[i] * (dataArray - mu[i])**2) /
                np.sum(gamaArray[i]))
        # 更新系数k
        for i in range(n):
            k[i] = np.sum(gamaArray[i]) / dataNum

    return [k, mu, sigma]


filename = r"/Users/francis/Desktop/代码/5号线/ultimate.csv"

if __name__ == '__main__':
    # 参数的准确值
    k = [0.5, 0.5]
    mu = [2, 4]
    sigma = [1, 1]
    # 样本数
    dataNum = 5000
    # 产生数据
    # dataArray = generateData(k,mu,sigma,dataNum)
    data = pd.read_csv(filename)
    dataArray = data['ww_time']
    # data2 =  data.values
    # dataArray = [[x] for x in data2]
    # 参数的初始值
    # 注意em算法对于参数的初始值是十分敏感的
    k0 = [0.8, 0.2]
    mu0 = [200, 300]
    sigma0 = [10, 12]
    step = 20
    # 使用em算法估计参数
    k1, mu1, sigma1 = em(dataArray, k0, mu0, sigma0, step)
    # 输出参数的值
    print("参数实际值:")
    print("k:", k)
    print("mu:", mu)
    print("sigma:", sigma)
    print("参数估计值:")
    print("k1:", k1)
    print("mu1:", mu1)
    print("sigma1:", sigma1)
    # print(dataArray)
    # print(data)

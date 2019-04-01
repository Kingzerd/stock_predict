import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn import datasets


class DimensionValueError(ValueError):
    """定义异常类"""
    pass


class PCA(object):
    """定义PCA类"""

    def __init__(self, x, n_components=None):
        """x的数据结构应为ndarray"""
        self.x = x
        self.dimension = x.shape[1]

        if n_components and n_components >= self.dimension:
            raise DimensionValueError("n_components error")

        self.n_components = n_components

    def cov(self):
        """求x的协方差矩阵"""
        x_T = np.transpose(self.x)  # 矩阵转秩
        # print(x_T)
        x_cov = np.cov(x_T)  # 协方差矩阵
        # print(x_cov)
        return x_cov

    def get_feature(self):
        """求协方差矩阵C的特征值和特征向量"""
        x_cov = self.cov()
        a, b = np.linalg.eig(x_cov)
        print(b.shape)
        print(b)
        m = a.shape[0]
        c = np.hstack((a.reshape((m, 1)), b))
        c_df = pd.DataFrame(c)
        # print(c_df)
        c_df_sort = c_df.sort_values(0, ascending=False)  # 按照特征值大小降序排列特征向量
        return c_df_sort

    def explained_varience_(self):
        c_df_sort = self.get_feature()
        # print(c_df_sort)
        return c_df_sort.values[:, 0]

    def paint_varience_(self):
        explained_variance_ = self.explained_varience_()
        plt.figure()
        plt.plot(explained_variance_, 'k')
        plt.xlabel('n_components', fontsize=16)
        plt.ylabel('explained_variance_', fontsize=16)
        plt.show()

    def reduce_dimension(self):
        """指定维度降维和根据方差贡献率自动降维"""
        c_df_sort = self.get_feature()
        varience = self.explained_varience_()

        if self.n_components:  # 指定降维维度
            p = c_df_sort.values[0:self.n_components, 1:]
            y = np.dot(p, np.transpose(self.x))  # 矩阵叉乘
            return np.transpose(y)

        varience_sum = sum(varience)  # 利用方差贡献度自动选择降维维度
        varience_radio = varience / varience_sum

        varience_contribution = 0
        for R in range(self.dimension):
            varience_contribution += varience_radio[R]  # 前R个方差贡献度之和
            if varience_contribution >= 0.99:
                break

        p = c_df_sort.values[0:R + 1, 1:]  # 取前R个特征向量
        # print(c_df_sort)
        # print(np.transpose(self.x))
        y = np.dot(p, np.transpose(self.x))  # 矩阵叉乘
        # self.paint_varience_()
        return np.transpose(y)

basic_path = os.path.dirname(os.path.abspath(__file__))
orgin_data_path = os.path.join(basic_path, "./dataset/datas1.csv")
# 读取原始数据，只保留需要使用的列
total_data = pd.read_csv(orgin_data_path,
                         usecols=["date", "r1", "r2", "r3", "r4","r5","r6"])
# 根据股票代码排序，相同的股票代码按照交易日期排序。
# inplace参数表示不需要返回排序后的结果，直接覆盖原变量即可
total_data.sort_values(by=['date'], inplace=True)
data = total_data.iloc[:, 1:6].values

print(data.shape)
x = data

print(x.shape)

if __name__ == '__main__':
    pca = PCA(x)
    y = pca.reduce_dimension()
    # print(y)
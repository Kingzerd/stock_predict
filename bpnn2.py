import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt


class Config:
    nn_input_dim = 2 #数组输入的维度是2（x,y两个坐标当然是二维啊）
    nn_output_dim = 2#数组输出的维度是2（分为两类当然是二维啊）
    epsilon = 0.01  # 梯度下降学习步长
    reg_lambda = 0.01  # 修正的指数?


def generate_data():
    np.random.seed(0)#伪随机数的种子0，当然也可以是1,2啊
    X, y = datasets.make_moons(200, noise=0.20)#产生200个数据，噪声误差为0.2
    return X, y


def visualize(X, y, model):
    plot_decision_boundary(lambda x:predict(model,x), X, y)#好好看这个代码，函数名字做参数哦
    plt.title("Logistic Regression")


def plot_decision_boundary(pred_func, X, y):
    #把X的第一列的最小值减掉0.5赋值给x_min，把X的第一列的最大值加0.5赋值给x_max
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # 根据最小最大值和一个网格距离生成整个网格,就是在图上细分好多个点，画分类边界的时候要用这些点
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
    plt.show()

def predict(model, x):
    #这是字典啊
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    z1 = x.dot(W1) + b1# 输入层向隐藏层正向传播
    a1 = np.tanh(z1) # 隐藏层激活函数使用tanh = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
    z2 = a1.dot(W2) + b2# 隐藏层向输出层正向传播
    exp_scores = np.exp(z2)#这两步表示输出层的激活函数为softmax函数哦
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return np.argmax(probs, axis=1)



def build_model(X, y, nn_hdim, num_passes=20000, print_loss=False):
    num_examples = len(X)
    np.random.seed(0)#初始化权值和偏置
    W1 = np.random.randn(Config.nn_input_dim, nn_hdim) / np.sqrt(Config.nn_input_dim)
    b1 = np.zeros((1, nn_hdim))
    W2 = np.random.randn(nn_hdim, Config.nn_output_dim) / np.sqrt(nn_hdim)
    b2 = np.zeros((1, Config.nn_output_dim))
    model = {}

    for i in range(0, num_passes):

        z1 = X.dot(W1) + b1# 输入层向隐藏层正向传播
        a1 = np.tanh(z1)# 隐藏层激活函数使用tanh = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
        z2 = a1.dot(W2) + b2# 隐藏层向输出层正向传播
        exp_scores = np.exp(z2)#这两步表示输出层的激活函数为softmax函数哦
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

        delta3 = probs
        #下面这才是delta3，为损失函数对z2求偏导数，y-y^
        delta3[range(num_examples), y] -= 1
        dW2 = (a1.T).dot(delta3)#损失函数对w2的偏导数
        db2 = np.sum(delta3, axis=0, keepdims=True)#损失函数对b2的偏导数
        delta2 = delta3.dot(W2.T) * (1 - np.power(a1, 2))#损失函数对z1的偏导数
        dW1 = np.dot(X.T, delta2)#损失函数对w1的偏导数
        db1 = np.sum(delta2, axis=0)#损失函数对b1的偏导数
        #个人认为下面两行代码完全没有必要存在
        dW2 += Config.reg_lambda * W2#w2梯度增量的修正  屁话
        dW1 += Config.reg_lambda * W1#w1梯度增量的修正  屁话
        #更新权值和偏置
        W1 += -Config.epsilon * dW1
        b1 += -Config.epsilon * db1
        W2 += -Config.epsilon * dW2
        b2 += -Config.epsilon * db2

        model = {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}

    return model


def main():
    X, y = generate_data()
    model = build_model(X, y, 8)
    visualize(X, y, model)


if __name__ == "__main__":
     main()
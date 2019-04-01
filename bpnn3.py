import tensorflow as tf
import numpy as np

# import matplot as plt

# create data
x_data = np.random.rand(200).astype(np.float32)
y_data = 0.1 * x_data + 0.3

# create structure of Neural Network
# 设置变量,并初始化
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))  # 权重初始值为-1到1之间的一个数
biases = tf.Variable(tf.zeros(1))  # 偏置初始值为0

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))  # 使用L1正则作为目标函数
# 设置优化器，使用梯度下降
optimizer = tf.train.GradientDescentOptimizer(0.5)  # 0.5为定义的学习率
train = optimizer.minimize(loss)  # 最小化目标函数

# init=tf.initialize_all_variables()#用于激活初始化函数
init = tf.global_variables_initializer()
# create structure end

# 激活tf中的会话
sess = tf.Session()
sess.run(init)

for step in range(201):  # 设置总的迭代步数为201步
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pso
import os

rnn_unit = 1  # 节点数目
input_size = 5
output_size = 1
data_train_begin_1 = 0
data_train_begin_2 = 300
data_train_end = 20
data_test_begin = 1440
data_test_end = 1800

# 定义权重和偏置
weights = {
    'in': tf.Variable(tf.random_normal([input_size, rnn_unit])),
    'out': tf.Variable(tf.random_normal([rnn_unit, 1]))
}
biases = {
    'in': tf.Variable(tf.constant(0.1, shape=[rnn_unit, ])),
    'out': tf.Variable(tf.constant(0.1, shape=[1, ]))
}


def get_train_data(batch_size=80, time_step=20, train_begin=data_train_begin_1, train_end=data_train_end):
    batch_index = []
    data_train = data[train_begin:train_end]

    # 标准化
    normalized_train_data = (data_train - np.mean(data_train, axis=0)) / np.std(data_train, axis=0)

    dim = input_size
    # size = train_end - train_begin
    size = rnn_unit
    iter_num = 5000
    x_max = 9999
    max_vel = 9999
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        pso_w = tf.random_normal([input_size, rnn_unit]).eval(session=sess)
        pso_b = tf.random_normal([rnn_unit, 1]).eval(session=sess)
    # print(normalized_train_data[:, 0:8].shape)
    # print(normalized_train_data[:, 8:9].shape)
    ps = pso.PSO(pso_w, pso_b, normalized_train_data[:, 0:input_size], normalized_train_data[:, input_size:], dim, size,
                 iter_num, x_max, max_vel)
    fit_var_list, best_pos, new_w, new_b = ps.update()

    # print(pso_w)
    print(new_w)
    print(new_b)

    new_data = np.dot(data_train[:, 0:input_size],new_w)+new_b
    t_data = data_train[:, input_size:]
    plt.figure()
    plt.plot(list(range(len(new_data))), new_data, color='b')
    plt.plot(list(range(len(t_data))), t_data, color='r')
    plt.legend(['predict', 'truth'])
    plt.show()


    # print(normalized_train_data[:, input_size:]-np.dot(normalized_train_data[:, 0:input_size],new_w)-new_b)

    weights['in'] = tf.Variable(new_w)
    biases['in'] = tf.Variable(new_b)

    # 训练集
    train_x, train_y = [], []

    # 此时normalized_train_data的shape是n*8
    for i in range(len(normalized_train_data) - time_step):  # i = 1~5785

        # 生成batch_index：0，batch_size*1，batch_size*2
        if i % batch_size == 0:
            batch_index.append(i)

        x = normalized_train_data[i:i + time_step, :input_size]  # x:shape 15*7
        y = normalized_train_data[i:i + time_step, input_size, np.newaxis]  # y:shape 15*1

        train_x.append(x.tolist())
        train_y.append(y.tolist())
    batch_index.append((len(normalized_train_data) - time_step))  # batch_index 收尾

    # train_x :n*15*7
    # train_y :n*15*1
    return batch_index, train_x, train_y


basic_path = os.path.dirname(os.path.abspath(__file__))
orgin_data_path = os.path.join(basic_path, "./dataset/datas1.csv")
# 读取原始数据，只保留需要使用的列
total_data = pd.read_csv(orgin_data_path,
                         usecols=["date", "r1", "r2", "r3", "r4","r5","r6"])
# 根据股票代码排序，相同的股票代码按照交易日期排序。
# inplace参数表示不需要返回排序后的结果，直接覆盖原变量即可
total_data.sort_values(by=['date'], inplace=True)
data = total_data.iloc[:, 1:].values
print(data.shape)
get_train_data()

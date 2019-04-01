# encoding: utf-8

'''

运行环境：
python：     3.6.2
tensorflow： 1.2
IDE：        pycharm
OS：         windows10

'''

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pso
import os

loss_record=[]
# 定义LSTM的超参数
# 根据股票历史数据中的最低价、最高价、开盘价、收盘价、交易量、交易额、跌涨幅等因素，对下一日股票最高价进行预测。
rnn_unit = 10  # 隐含层节点数目
input_size = 5
output_size = 1
lr = 0.001  # 学习率
layer_num = 2
data_train_begin_1 = 0
data_train_begin_2 = 300
data_train_end = 1440
data_test_begin = 1440
data_test_end = 1780

# 定义权重和偏置
weights = {
    'in': tf.Variable(tf.random_normal([input_size, rnn_unit])),
    'out': tf.Variable(tf.random_normal([rnn_unit, 1]))
}
biases = {
    'in': tf.Variable(tf.constant(0.1, shape=[rnn_unit, ])),
    'out': tf.Variable(tf.constant(0.1, shape=[1, ]))
}

'''
函数功能：获取获取训练数据，从原始数据中整理出训练数据
@:param batch_size  批大小
@:param time_step   时间步
@:param train_begin 训练起始点
@:param train_end   训练终止点

@:return    batch_index（批索引）、train_x（训练数据feature）train_y（训练数据label）
'''


def get_train_data(batch_size=80, time_step=20, train_begin=data_train_begin_1, train_end=data_train_end):
    batch_index = []
    data_train = data[train_begin:train_end]

    # 标准化
    normalized_train_data = (data_train - np.mean(data_train, axis=0)) / np.std(data_train, axis=0)

    dim = input_size
    # size = train_end - train_begin
    size = rnn_unit
    iter_num = 10000
    x_max = 9999
    max_vel = 9999
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        pso_w = tf.random_normal([input_size, rnn_unit]).eval(session=sess)
        pso_b = tf.random_normal([rnn_unit, 1]).eval(session=sess)
    # print(normalized_train_data[:, 0:8].shape)
    # print(normalized_train_data[:, 8:9].shape)
    ps = pso.PSO(pso_w, pso_b, normalized_train_data[:, 0:input_size], normalized_train_data[:, input_size:], dim, size, iter_num, x_max, max_vel)
    fit_var_list, best_pos, new_w, new_b = ps.update()

    print(pso_w)
    print(new_w)
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


'''
函数功能：获取测试数据

@:param time_step   时间步
@:param test_begin  起始点

@:return    预测值、最终状态
'''


def get_test_data(time_step=20, test_begin=data_test_begin):
    data_test = data[test_begin:data_test_end]  # 截取测试数据
    mean = np.mean(data_test, axis=0)  # 平均数
    std = np.std(data_test, axis=0)  # 方差
    normalized_test_data = (data_test - mean) / std  # 标准化

    # 有size个sample
    size = (len(normalized_test_data) + time_step - 1) // time_step
    test_x, test_y = [], []

    for i in range(size - 1):
        x = normalized_test_data[i * time_step:(i + 1) * time_step, :input_size]  # x shape 20*7
        y = normalized_test_data[i * time_step:(i + 1) * time_step, input_size]  # y shape (20,)
        test_x.append(x.tolist())
        test_y.extend(y)

    # 保存得到的x和y
    test_x.append((normalized_test_data[(i + 1) * time_step:, :input_size]).tolist())  # shape 16*20*7
    test_y.extend((normalized_test_data[(i + 1) * time_step:, input_size]).tolist())  # shape 309
    return mean, std, test_x, test_y


'''
函数功能：构造LSTM网络模型

@:param X   数据的label  shape = [None,time_step,input_size]
@:return    预测值、最终状态
'''


def lstm(X):
    batch_size = tf.shape(X)[0]  # 获取batch_size值
    time_step = tf.shape(X)[1]  # 获取time_step值
    w_in = weights['in']
    b_in = biases['in']

    input = tf.reshape(X, [-1, input_size])  # 需要将tensor转成2维进行计算，计算后的结果作为隐藏层的输入 系统的输入单元数为7，所以将输入数据shape为n行7列
    input_rnn = tf.matmul(input, tf.cast(w_in,tf.float32)) + tf.cast(b_in,tf.float32)  # 输入数据与输入权重相乘，得到输入数据对隐含层的影响
    # input_rnn = tf.nn.dropout(tf.nn.relu_layer(input, w_in, b_in), 0.8)
    input_rnn = tf.nn.tanh(input_rnn)

    # 将tensor转成3维，作为lstm cell的输入
    # 隐含层的cell接收的数据是3维的，即将n*10的数据shape为n*15*10的数据
    input_rnn = tf.reshape(input_rnn, [-1, time_step, rnn_unit])

    # 设置lstm的cell，BasicLSTMCell的入参有(self, num_units, forget_bias=1.0,state_is_tuple=True, activation=None, reuse=None)
    # 此处只设置其隐含层数目为rnn_unit，其他参数使用默认值
    # cell = tf.nn.rnn_cell.BasicLSTMCell(rnn_unit)
    cell = tf.contrib.rnn.MultiRNNCell([tf.nn.rnn_cell.BasicLSTMCell(rnn_unit) for _ in range(layer_num)],
                                       state_is_tuple=True)
    init_state = cell.zero_state(batch_size, dtype=tf.float32)

    # output_rnn是记录LSTM每个输出节点的结果，final_states是最后一个cell的结果
    output_rnn, final_states = tf.nn.dynamic_rnn(cell, input_rnn, initial_state=init_state, dtype=tf.float32)

    # 将输出数据shape为n*10格式
    output = tf.reshape(output_rnn, [-1, rnn_unit])

    w_out = weights['out']
    b_out = biases['out']

    # cell输出经过与输出权重矩阵相乘并加入偏置后，得到最终输出
    pred = tf.matmul(output, w_out) + b_out
    print(w_out.shape)
    print(w_out)
    print(b_out.shape)
    print(b_out)

    return pred, final_states


'''
函数功能：训练模型
@:param batch_size      批大小
@:param time_step       时间步长度
@:param train_begin     训练起始
@:param train_end       训练截止
@:return                打印得分并将模型保存
'''


def train_lstm(batch_size=80, time_step=15, train_begin=data_train_begin_2, train_end=data_train_end):
    # X是训练数据中的feature Y是训练数据中的label
    X = tf.placeholder(tf.float32, shape=[None, time_step, input_size])
    Y = tf.placeholder(tf.float32, shape=[None, time_step, output_size])

    # 获取训练数据  batch_index:80的等差序列 train_x：[3785*15] train_y:[3785*15]  15:time_step值
    batch_index, train_x, train_y = get_train_data(batch_size, time_step, train_begin, train_end)




    # 创建预测值获取的计算流程
    with tf.variable_scope("sec_lstm"):
        pred, _ = lstm(X)

    # 创建损失函数的计算流程
    loss = tf.reduce_mean(tf.square(tf.reshape(pred, [-1]) - tf.reshape(Y, [-1])))

    # 定义优化函数（即训练使）
    train_op = tf.train.AdamOptimizer(lr).minimize(loss)

    # 将变量保存
    saver = tf.train.Saver(tf.global_variables())  # max_to_keep = 15

    with tf.Session() as sess:
        try:
            module_file = tf.train.latest_checkpoint('.')
            saver.restore(sess, module_file)
        except:
            sess.run(tf.global_variables_initializer())

        # 重复训练
        for i in range(11):
            # 按批次进行训练，每一批次80条数据
            for step in range(len(batch_index) - 1):
                _, loss_ = sess.run([train_op, loss], feed_dict={X: train_x[batch_index[step]:batch_index[step + 1]],
                                                                 Y: train_y[batch_index[step]:batch_index[step + 1]]})
            if i % 200 == 0:
                print("保存模型：", saver.save(sess, './model_save_pro/model/stock2.model', global_step=i))
                # writer = tf.summary.FileWriter("F:\PythonPrograms\stock_predict\model_save_pro\model", sess.graph)
            print(i, loss_)
            loss_record.append(loss_)
        # writer.close()


'''
函数功能：根据模型进行预测

@:param time_step       时间步长度
@:return                打印得分并将模型保存
'''


def prediction(time_step=20):
    X = tf.placeholder(tf.float32, shape=[None, time_step, input_size])
    # Y=tf.placeholder(tf.float32, shape=[None,time_step,output_size])

    # 获取测试数据的“均值”、“方差”、feature和label
    # test_x 16*20（最后一个长度为9） test_y：309
    mean, std, test_x, test_y = get_test_data(time_step)

    with tf.variable_scope("sec_lstm", reuse=True):
        pred, _ = lstm(X)

    saver = tf.train.Saver(tf.global_variables())

    time_line = []
    for i in range(1987, 2017):
        for j in range(1, 13):
            time_line.append(str(i)+'-'+str(j))
    print(time_line)

    with tf.Session() as sess:
        # 参数恢复
        module_file = tf.train.latest_checkpoint('./model_save_pro/model/')
        saver.restore(sess, module_file)
        test_predict = []
        for step in range(len(test_x)):  # 原为len(test_x) - 1
            prob = sess.run(pred, feed_dict={X: [test_x[step]]})  # prob是长度为20的一维矩阵，也就是说，对于我们的模型，输入是15，输出是20
            predict = prob.reshape((-1))
            test_predict.extend(predict)
        test_y = np.array(test_y) * std[input_size] + mean[input_size]
        test_predict = np.array(test_predict) * std[input_size] + mean[input_size]
        acc = np.average(np.abs(test_predict - test_y[:len(test_predict)]) / test_y[:len(test_predict)])  # 偏差
        print("偏差：", acc)
        writer = tf.summary.FileWriter("F:\PythonPrograms\stock_predict\model_save_pro\model", sess.graph)

        # 以折线图表示结果
        # plt.figure()
        # plt.plot(time_line[:340], test_predict, color='b')
        # plt.plot(time_line[:340], test_y, color='r')
        # plt.legend(['predict', 'truth'])
        # plt.show()

        fig1 = plt.figure(figsize=(45, 5))
        ax1 = fig1.add_subplot(1, 1, 1)
        # ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 设置时间标签显示格式
        # plt.xticks(pd.date_range('1987-01-01', '1988-01-01'), rotation=90)
        plt.xticks(range(len(time_line[:60])),time_line[:60], rotation=90)
        # plt.ylim(40000,65000)
        for x, y in zip(range(len(time_line[:60])), test_y[:60]):
            plt.text(x, y + 0.3, '%.0f' % y, ha='center', va='bottom', fontsize=10.5)
        plt.title("北美洲")
        plt.plot(test_y[:60], '.-')
        plt.show()


# ========================================主代码==================================

# 导入数据
# f = open('dataset/dataset_2.csv')
# df = pd.read_csv(f)  # 读入股票数据
# data = df.iloc[:, 2:10].values  # 取第3-10列   data实际数据大小[6109 * 8]

basic_path = os.path.dirname(os.path.abspath(__file__))
orgin_data_path = os.path.join(basic_path, "./dataset/datas1.csv")
# 读取原始数据，只保留需要使用的列
total_data = pd.read_csv(orgin_data_path,
                         usecols=["date", "r1", "r2", "r3", "r4","r5","r6"])
# 根据股票代码排序，相同的股票代码按照交易日期排序。
# inplace参数表示不需要返回排序后的结果，直接覆盖原变量即可
total_data.sort_values(by=['date'], inplace=True)
data = total_data.iloc[:, 1:].values

# 内部调用了get_train_data函数，从data中获取了训练数据
# 获取训练数据  batch_index:80的等差序列 train_x：[3785*15] train_y:[3785*15]  15:time_step值
# 默认取2000~5800之间的数据作为训练数据，
train_lstm()

# 内部调用了get_test_data函数，从data中获取了测试函数
# 取5800往后的数据作为测试数据，一共309个数据
# test_x 16*20（最后一个长度为9） test_y：309
prediction()

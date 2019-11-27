import tensorflow as tf
import numpy as np
import time

import readmidi_nn
import data_set_nn

playlist = readmidi_nn.readmidi("/sampleMidi/moonlight.mid")
x_input,y_target = readmidi_nn.makeMidi_nn(playlist,24)
batch_feeder = data_set_nn.data_set_nn(x_input,y_target)
length = len(playlist)

"""
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
"""
###load saved Weight, bias
#s_W1=np.load("W1.npy")
#s_b1=np.load("b1.npy")

#s_W2=np.load("W2.npy")
#s_b2=np.load("b2.npy")

#W1 = tf.Variable(s_W1)
#b1 = tf.Variable(s_b1)
#W2 = tf.Variable(s_W2)
#b2 = tf.Variable(s_b2)
###End load

###if not load, define W1,W2,b1,b2 
x = tf.placeholder(tf.float32,[None,24 * 88])
W1 = tf.Variable(tf.random_normal([24 * 88,88]))
#W1 = tf.Variable(s_W1,88)
b1 = tf.Variable(tf.zeros([88]))

h = tf.nn.softmax(tf.matmul(x, W1) + b1)
W2 = tf.Variable(tf.random_normal([88,88]))
#W2 = tf.Variable(tf.convert_to_tensor(np.eye(88), dtype=tf.float32))
b2 = tf.Variable(tf.random_normal([88]))

y = tf.nn.softmax(tf.matmul(h, W2) + b2)

y_ = tf.placeholder(tf.float32, [None, 88] ) # want

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

iteration1 =200
iteration2 =5000
##########
for itr in range(iteration1):
    for i in range(iteration2):
        """
       batch_xs, batch_ys = mnist.train.next_batch(100)
       """
        x_input_batch, y_target_batch = batch_feeder.get_next_batch(size=100)
        sess.run(train_step, feed_dict={x: x_input_batch, y_: y_target_batch})
        # test output
        if i % 100 == 0:
            print(i+itr*iteration2)
    
    ###print trained playlist
    playlist = []
    x_input_batch, y_target_batch = batch_feeder.get_next_batch(size=1)
    for i in range(length):
        playone = []
        _y = sess.run(y, feed_dict={x: x_input_batch})
        for j in _y:
            hum = 0
            hum_arr = []
            note = 1
            for k in j:
                if (k > 0.2):
                    hum_arr.append(k)
                    hum += 1
                if (k > 0.2):
                    playone.append(note)
                note = note + 1
            # print hum, hum_arr
            playlist.append(playone)

        next = []
        for i in range(1, 89):
            if i in playone:
                next.append(1)
            else:
                next.append(0)
        # print x_input_batch, [next]
        x_input_batch = np.append(x_input_batch[0][88:], next)
        x_input_batch = np.asarray([x_input_batch])
        # print x_input_batch
    print (playlist)
    
    ###Save Weigth,bias
    np.save('W1',W1.eval(session=sess),x)
    np.save('b1',b1.eval(session=sess),x)

    np.save('W2',W2.eval(session=sess),x)
    np.save('b2',b2.eval(session=sess),x)




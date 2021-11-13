import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import matplotlib.pyplot as plt

def train_model():
    x_train = np.arange(10)
    #print("x_train", x_train)
    y_train = [ 5*i**2+7*i+9 for i in x_train]

    X = tf.placeholder("float")
    Y = tf.placeholder("float")

    a = tf.Variable(np.random.randn(), name = "a")
    b = tf.Variable(np.random.randn(), name = "b")
    c = tf.Variable(np.random.randn(), name = "c")

    learning_rate = 0.005
    epochs = 5000

    deg = a*tf.pow(X,2) + b*X + c
    mse = tf.reduce_sum(tf.pow(deg - Y, 2)) / (2 * 10)
    optimizer = tf.train.AdamOptimizer(learning_rate).minimize(mse)

    init = tf.global_variables_initializer()
    
    with tf.Session() as session:
        session.run(init)
        for epoch in range(epochs):
            for (x,y) in zip(x_train, y_train):
                session.run(optimizer, feed_dict={X:x, Y:y})
            if (epoch + 1 ) % 100 == 0:
                cost = session.run(mse,feed_dict={X:x_train, Y:y_train})
                print("Epoch",(epoch + 1), ": Training Cost:", cost," a, b, c = ",session.run(a),', ',session.run(b),', ',session.run(c),'\n')
                A = session.run(a)
                B = session.run(b)
                C = session.run(c)

    return A,B,C

def test_model(a,b,c):
    for i in range(10):
        print('for input ',i,' the output is :',np.round((a * (i** 2)) + (b * i) + c))


if __name__ == '__main__':
    a,b,c = train_model()
    test_model(a,b,c)
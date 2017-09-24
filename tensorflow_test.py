import tensorflow as tf

node_1 = tf.constant([5.7, 6, 7, 8, 9], name='list1')
node_2 = tf.constant([1, 2.0, 3, 4, 5], name='list2')

addition = tf.add(node_1, node_2, name='addition')

first = tf.placeholder(tf.float32, name='firstElement')
second = tf.placeholder(tf.float32, name='secondElement')
summation = tf.add(first, second, name='summation')

product = tf.multiply(addition, summation, name='product')

y_intercept = tf.Variable([.3], name='intercept')
slope = tf.Variable([-.3], name='slope')
x = tf.placeholder(tf.float32,name='x')

linear_model = slope*x + y_intercept

init = tf.global_variables_initializer()

with tf.Session() as sess:
    # print sess.run(node_1)
    # print sess.run(node_2)
    # print sess.run(product, {first: 9.8, second: 7.6})
    sess.run(init)
    print sess.run(linear_model, {x: [1, 2, 3, 4]})

    writer = tf.summary.FileWriter("/Users/espunky/Machine-Learning/", sess.graph)

writer.close()
sess.close()
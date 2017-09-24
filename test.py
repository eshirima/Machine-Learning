import tensorflow as tf

result = tf.add(5, 3)

another = tf.add(8, 5)

product = tf.multiply(result, another)

with tf.Session() as sess:
    print(sess.run(product))
    print(result)

    writer = tf.summary.FileWriter("/Users/espunky/Machine-Learning/", sess.graph)

writer.close()
sess.close()
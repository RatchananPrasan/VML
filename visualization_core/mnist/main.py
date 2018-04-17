from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from model import cnn_model_fn
import sample

def main(unused_argv):

  size, sample_2d = sample.input_sample_2d()

  plt.imshow(sample_2d)
  plt.show()

  '''
  mnist_classifier = tf.estimator.Estimator(
      model_fn=cnn_model_fn, model_dir="saved")

  latest_checkpoint = mnist_classifier.latest_checkpoint()

  with tf.Session() as sess:
    saver = tf.train.import_meta_graph(latest_checkpoint + ".meta")
    saver.restore(sess, tf.train.latest_checkpoint("mnist_model"))

    graph = tf.get_default_graph()
    for i in graph.get_operations():
        print(i.name)

    for i in graph.get_collection("trainable_variables"):
        print(i)
  
  
  names = mnist_classifier.get_variable_names()

  for i in names:
      print("Layer :", i, mnist_classifier.get_variable_value(i).shape)

  conv2d_kernel = mnist_classifier.get_variable_value('conv2d/kernel')
  print(conv2d_kernel.shape)
  
  data = []

  for i in range(32):
      data.append(list())
      for j in range(5):
          data[i].append(list())
          for k in range(5):
              data[i][j].append(conv2d_kernel[j][k][0][i])

  rows = 4
  cols = 8
  current = 1
  for i in data:
      plt.subplot(rows, cols , current)
      plt.imshow(i, cmap="gray")
      current += 1
  plt.show()
  '''

if __name__ == "__main__":
  tf.app.run()
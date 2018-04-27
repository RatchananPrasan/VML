import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from .helper import get_mnist_filename
from .vis_graph import VisGraph

class MnistVisualizer():

    def __init__(self, input_file, graph_generator):

        self.filename = get_mnist_filename()
        self.input_file = input_file
        self.graph_generator = graph_generator

        self.meta = {
            "layers" : [
                "Input Layer : 28x28 Monochrome Image",
                "Convolution Layer #1 : 32 5x5 filters with Relu",
                "Pooling Layer #1 : Max Pooling, size=2x2, strides=2",
                "Convolution Layer #2 : 64 5x5 filters with Relu",
                "Pooling Layer #2 : Max Pooling, size=2x2, strides=2",
                "Dense Layer #1 : 256 units with Relu",
                "Dense Layer #2 : 10 units"
            ]
        }

        #self.input_tensor = self._read_image()

        self._read_variables()

        self._gen_graph()


    def get_meta(self):
        return self.meta


    def get_graph_meta(self):
        return self.graph_generator.get_graph_meta()


    def get_data(self):
        return self.graph_generator.get_data()


    def get_dotstring(self):
        return self.graph_generator.get_dotstring()


    def _read_image(self):
        # Not usable yet

        with open(self.input_file, "rb") as file_obj:

            image_raw = file_obj.read()

        with tf.Graph().as_default():

            image_op = tf.image.decode_jpeg(image_raw, channels=4)
            resize_op = tf.image.resize_images(image_op, [28, 28], 
                method=tf.image.ResizeMethod.AREA)

            with tf.Session() as sess:

                image = sess.run(resize_op)
                print(image[:, :, 3])
                image_resized = sess.run(tf.reshape(image[:, :, 0], shape=[784]))

        return image_resized


    def _read_variables(self):

        with tf.Graph().as_default():

            with tf.Session() as sess:
                
                saver = tf.train.import_meta_graph(self.filename + ".meta")
                saver.restore(sess, self.filename)

                self.conv_1_kernel = sess.run("conv2d/kernel:0")
                self.conv_1_bias = sess.run("conv2d/bias:0")

                self.conv_2_kernel = sess.run("conv2d_1/kernel:0")
                self.conv_2_bias = sess.run("conv2d_1/bias:0")

                self.dense_1_kernel = sess.run("dense/kernel:0")
                self.dense_1_bias = sess.run("dense/bias:0")

                self.dense_2_kernel = sess.run("dense_1/kernel:0")
                self.dense_2_bias = sess.run("dense_1/bias:0")


    def _gen_graph(self):
        
        with tf.Graph().as_default():

            data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.023529414, 0.76470596, 0.9960785, 1.0, 0.93725497, 0.1137255, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.023529414, 0.6392157, 0.9960785, 0.9960785, 0.6862745, 0.21568629, 0.011764707, 0.0, 0.0, 0.0, 0.0, 0.09019608, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.47450984, 0.9960785, 0.9960785, 0.5803922, 0.03137255, 0.0, 0.0, 0.0, 0.0, 0.0, 0.54901963, 0.9294118, 0.43921572, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.16862746, 0.9607844, 0.9960785, 0.9490197, 0.015686275, 0.0, 0.0, 0.0, 0.0, 0.0, 0.20784315, 0.92549026, 0.9960785, 0.43921572, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6431373, 0.9960785, 0.9803922, 0.2509804, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6627451, 0.9960785, 0.97647065, 0.1254902, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.83921576, 0.9960785, 0.69803923, 0.0, 0.0, 0.011764707, 0.03529412, 0.03529412, 0.03529412, 0.17254902, 0.909804, 0.9960785, 0.64705884, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.83921576, 0.9960785, 0.7254902, 0.0, 0.21176472, 0.7294118, 0.9960785, 0.9960785, 0.9960785, 0.9960785, 0.9960785, 0.9058824, 0.16862746, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.37647063, 0.9960785, 0.9803922, 0.74509805, 0.98823535, 0.9960785, 0.9960785, 0.9960785, 0.9960785, 0.9960785, 0.9960785, 0.50980395, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.49411768, 0.9960785, 0.9960785, 0.9960785, 0.9960785, 0.7803922, 0.46274513, 0.5686275, 0.9960785, 0.9960785, 0.9960785, 0.30588236, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.10980393, 0.47058827, 0.47058827, 0.47058827, 0.1254902, 0.011764707, 0.0, 0.47450984, 0.9960785, 0.9960785, 0.76470596, 0.015686275, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.43137258, 0.9960785, 0.9960785, 0.33333334, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.41960788, 0.9960785, 0.98823535, 0.19215688, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8235295, 0.9960785, 0.7176471, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.058823533, 0.87843144, 0.9960785, 0.2784314, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.27058825, 0.9960785, 0.97647065, 0.20784315, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8470589, 0.9960785, 0.92549026, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8745099, 0.9960785, 0.74509805, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8745099, 0.9960785, 0.73333335, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8745099, 0.9960785, 0.97647065, 0.49411768, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.44705886, 0.9333334, 0.9960785, 0.48627454, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        
            image_raw = tf.convert_to_tensor(data)

            image_input = tf.reshape(image_raw, [1, 28, 28, 1])

            conv_1 = tf.layers.conv2d(inputs=image_input,
                filters=32,
                kernel_size=[5, 5],
                padding="same",
                activation=tf.nn.relu,
                kernel_initializer=tf.constant_initializer(self.conv_1_kernel),
                bias_initializer=tf.constant_initializer(self.conv_1_bias))

            pool_1 = tf.layers.max_pooling2d(inputs=conv_1,
                pool_size=[2, 2],
                strides=2)

            conv_2 =  tf.layers.conv2d(inputs=pool_1,
                filters=64,
                kernel_size=[5, 5],
                padding="same",
                activation=tf.nn.relu,
                kernel_initializer=tf.constant_initializer(self.conv_2_kernel),
                bias_initializer=tf.constant_initializer(self.conv_2_bias))

            pool_2 = tf.layers.max_pooling2d(inputs=conv_2,
                pool_size=[2, 2],
                strides=2)

            pool_2_flat = tf.reshape(pool_2, [1, 7 * 7 * 64])

            dense_1 = tf.layers.dense(inputs=pool_2_flat,
                units=256,
                activation=tf.nn.relu,
                kernel_initializer=tf.constant_initializer(self.dense_1_kernel),
                bias_initializer=tf.constant_initializer(self.dense_1_bias))

            dense_2 = tf.layers.dense(inputs=dense_1,
                units=10,
                kernel_initializer=tf.constant_initializer(self.dense_2_kernel),
                bias_initializer=tf.constant_initializer(self.dense_2_bias))

            detected_class = tf.argmax(input=dense_2, axis=1)

            probabilities = tf.nn.softmax(dense_2)

            init = tf.global_variables_initializer()

            with tf.Session() as sess:

                sess.run(init)

                image_input_out = sess.run(image_input)
                image_input_out = image_input_out[0, :, :, 0]
                image_input_out_np = np.reshape(image_input_out, (28 * 28))
                self.graph_generator.draw_input(image_input_out_np, (28 , 28))

                conv_1_out = sess.run(conv_1)
                self.graph_generator.draw_convolution(conv_1_out, (28, 28), 
                    self.conv_1_kernel, (5, 5), "Relu")

                pool_1_out = sess.run(pool_1)
                self.graph_generator.draw_pooling(pool_1_out, (14, 14))

                conv_2_out = sess.run(conv_2)
                self.graph_generator.draw_convolution(conv_2_out, (14, 14),
                    self.conv_2_kernel, (5,5), "Relu")

                pool_2_out = sess.run(pool_2)
                self.graph_generator.draw_pooling(pool_2_out, (7, 7))

                self.graph_generator.end_dotstring()

                detected_class_out = sess.run(detected_class)
                probabilities_out = sess.run(probabilities)

                self.meta["output"] = detected_class_out[0]
                probs = {}
                for index, num in enumerate(probabilities_out[0]):
                    probs[index] = float(num * 100)
                self.meta["probabilities"] = probs
                

if __name__ == "__main__":

    mnist = MnistVisualizer("", VisGraph())

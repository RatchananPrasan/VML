import tensorflow as tf

import helper as hp
import operations as ops

class ModelReader():

    def __init__(self, filename):
        self.filename = filename
        self.operations = []
        self._read_operation()


    def get_operations(self):
        return self.operations


    def _read_operation(self):

        with tf.Graph().as_default():

            with tf.Session() as sess:

                saver = tf.train.import_meta_graph(self.filename + ".meta")
                saver.restore(sess, self.filename)

                graph = tf.get_default_graph()
                for i in graph.get_operations():
                    
                    if (i.type in ops.Available_ops):
                        name = i.name.split("/")[0]

                        if (i.type == ops.CONV2D):
                            padding = i.get_attr("padding").decode("utf-8")
                            strides = i.get_attr("strides")[1:3]
                            conv_2d = ops.Convolutional2D_OP(padding, strides)
                            for j in graph.get_collection("trainable_variables"):
                                compared_name = j.name.split("/")[0]
                                if (name == compared_name):
                                    if ("kernel" in j.name):
                                        kernel = sess.run(j)
                                        conv_2d.set_kernel(kernel)
                                    elif ("bias" in j.name):
                                        bias = sess.run(j)
                                        conv_2d.set_bias(bias)
                            self.operations.append(conv_2d)
                            
                        elif (i.type == ops.MAXPOOL2D):
                            padding = i.get_attr("padding").decode("utf-8")
                            strides = i.get_attr("strides")[1:3]
                            pool_size = i.get_attr("ksize")[1:3]
                            pool_2d = ops.MaxPooling2D_OP(pool_size, padding, strides)
                            self.operations.append(pool_2d)

                        elif(i.type == ops.AVGPOOL2D):
                            padding = i.get_attr("padding").decode("utf-8")
                            strides = i.get_attr("strides")[1:3]
                            pool_size = i.get_attr("ksize")[1:3]
                            pool_2d = ops.AvgPooling2D_OP(pool_size, padding, strides)
                            self.operations.append(pool_2d)

                        elif (i.type == ops.DENSE):
                            found_kernel = False
                            dense = ops.Dense_OP()
                            for j in graph.get_collection("trainable_variables"):
                                compared_name = j.name.split("/")[0]
                                if (name == compared_name):
                                    if ("kernel" in j.name):
                                        kernel = sess.run(j)
                                        dense.set_kernel(kernel)
                                        found_kernel = True
                                    elif ("bias" in j.name):
                                        bias = sess.run(j)
                                        dense.set_bias(bias)
                            if (found_kernel):
                                self.operations.append(dense)

                    elif (i.type in ops.Activation_ops):
                        if (i.type == ops.RELU):
                            self.operations[-1].set_activation(tf.nn.relu)
import tensorflow as tf

RELU = "Relu"
CONV2D = "Conv2D"
DENSE = "MatMul"
AVGPOOL2D = "AvgPool"
MAXPOOL2D = "MaxPool"
INPUT = "Input"
FLAT = "Flat"

Available_ops = set([
    CONV2D, DENSE, AVGPOOL2D, MAXPOOL2D
])

Activation_ops = set([
    RELU
])

class Base_OP():

    def type(self):
        pass

    def gen_op(self, inputs):
        pass

    def to_string(self):
        pass


class Convolutional2D_OP(Base_OP):

    def __init__(self, padding, strides):
        self.padding = padding
        self.strides = strides
        self.kernel = None
        self.kernel_size = []
        self.kernel_num = None
        self.bias = None
        self.activation = None

    
    def type(self):
        return CONV2D


    def to_string(self):
        result = "Convolutional Layer :"
        result += " " + str(self.kernel_num)
        result += " " + str(self.kernel_size[0]) + "x" + str(self.kernel_size[1]) + " filters"
        result += ", padding=" + self.padding
        result += ", strides=" + str(self.strides)
        if (self.activation is not None):
            # TO-DO Handle Other Activation Function
            result += " with " + RELU

        return result


    def set_kernel(self, kernel):
        self.kernel = kernel
        self.kernel_num = kernel.shape[3]
        self.kernel_size.append(kernel.shape[0])
        self.kernel_size.append(kernel.shape[1])


    def set_bias(self, bias):
        self.bias = bias


    def set_activation(self, activation):
        self.activation = activation

    
    def gen_op(self, inputs):
        kernel = tf.constant_initializer(self.kernel)
        if (self.bias is not None):
            bias = tf.constant_initializer(self.bias)
        else:
            bias = tf.zeros_initializer()
        operation = tf.layers.conv2d(inputs=inputs, 
            filters=self.kernel_num,
            kernel_size=self.kernel_size,
            strides=self.strides,
            padding=self.padding,
            activation=self.activation,
            kernel_initializer=kernel,
            bias_initializer=bias)

        return operation


class AvgPooling2D_OP(Base_OP):

    def __init__(self, pool_size, padding, strides):
        self.pool_size = pool_size
        self.padding = padding
        self.strides = strides

    
    def type(self):
        return AVGPOOL2D


    def to_string(self):
        result = "Pooling Layer : Average Pooling"
        result += ", pool_size=" + str(self.pool_size)
        result += ", padding=" + self.padding
        result += ", strides=" + str(self.strides)

        return result

    
    def gen_op(self, inputs):
        operation = tf.layers.average_pooling2d(inputs=inputs,
            pool_size=self.pool_size,
            strides=self.strides,
            padding=self.padding)

        return operation


class MaxPooling2D_OP(Base_OP):

    def __init__(self, pool_size, padding, strides):
        self.pool_size = pool_size
        self.padding = padding
        self.strides = strides

    
    def type(self):
        return MAXPOOL2D


    def to_string(self):
        result = "Pooling Layer : Max Pooling"
        result += ", pool_size=" + str(self.pool_size)
        result += ", padding=" + self.padding
        result += ", strides=" + str(self.strides)

        return result

    
    def gen_op(self, inputs):
        operation = tf.layers.max_pooling2d(inputs=inputs,
            pool_size=self.pool_size,
            strides=self.strides,
            padding=self.padding)

        return operation


class Dense_OP(Base_OP):

    def __init__(self):
        self.kernel = None
        self.bias = None
        self.units = None
        self.activation = None


    def type(self):
        return DENSE


    def to_string(self):
        result = "Dense Layer :"
        result += " " + str(self.units) + " units"
        if (self.activation is not None):
            # TO-DO Handle Other Activation Function
            result += " with " + RELU
        return result


    def set_kernel(self, kernel):
        self.kernel = kernel
        self.units = kernel.shape[1]


    def set_bias(self, bias):
        self.bias = bias


    def set_activation(self, activation):
        self.activation = activation


    def gen_op(self, inputs):
        kernel = tf.constant_initializer(self.kernel)
        if (self.bias is not None):
            bias = tf.constant_initializer(self.bias)
        else:
            bias = tf.zeros_initializer()
        operation = tf.layers.dense(inputs=inputs, 
            units=self.units,
            activation=self.activation,
            kernel_initializer=kernel,
            bias_initializer=bias)

        return operation


class Input_OP(Base_OP):

    def __init__(self, image_width, image_height, channel):
        self.image_width = image_width
        self.image_height = image_height
        self.channel = channel

    
    def type(self):
        return INPUT


    def gen_op(self, inputs):
        image_raw = tf.convert_to_tensor(inputs)
        operation = tf.reshape(image_raw, [1, self.image_width, self.image_height, self.channel])
        return operation


    def to_string(self):
        result = "Input Layer:"
        result += " " + str(self.image_width) + "x" + str(self.image_height)
        result += " channel=" + str(self.channel)
        
        return result


class Flat_OP(Base_OP):

    def __init__(self, width, height, amount):
        self.width = width
        self.height = height
        self.amount = amount

    
    def type(self):
        return FLAT


    def gen_op(self, inputs):
        operation = tf.reshape(inputs, [1, self.width * self.height * self.amount])
        return operation


    def to_string(self):
        result = "Flat Layer : " + str(self.width * self.height * self.amount) + " pixels"
        return result
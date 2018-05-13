import tensorflow as tf

RELU = "Relu"
CONV2D = "Conv2D"
DENSE = "MatMul"
AVGPOOL2D = "AvgPool"
MAXPOOL2D = "MaxPool"

Available_ops = set([
    CONV2D, DENSE, AVGPOOL2D, MAXPOOL2D
])

Activation_ops = set([
    RELU
])

class BaseOp():

    def type(self):
        pass

    def gen_op(self, inputs):
        pass

    def to_string(self):
        pass


class Convolutional2D_OP(BaseOp):

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
        result += ", padding=" + self.padding.decode("utf-8")
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
        pass


class AvgPooling2D_OP(BaseOp):

    def __init__(self, pool_size, padding, strides):
        self.pool_size = pool_size
        self.padding = padding
        self.strides = strides

    
    def type(self):
        return AVGPOOL2D


    def to_string(self):
        result = "Pooling Layer : Average Pooling"
        result += ", pool_size=" + str(self.pool_size)
        result += ", padding=" + self.padding.decode("utf-8")
        result += ", strides=" + str(self.strides)

        return result

    
    def gen_op(self, inputs):
        pass


class MaxPooling2D_OP(BaseOp):

    def __init__(self, pool_size, padding, strides):
        self.pool_size = pool_size
        self.padding = padding
        self.strides = strides

    
    def type(self):
        return MAXPOOL2D


    def to_string(self):
        result = "Pooling Layer : Max Pooling"
        result += ", pool_size=" + str(self.pool_size)
        result += ", padding=" + self.padding.decode("utf-8")
        result += ", strides=" + str(self.strides)

        return result

    
    def gen_op(self, inputs):
        pass


class Dense_OP(BaseOp):

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
        pass
import os

def get_mnist_filename():

    result = os.path.abspath(os.path.dirname(__file__))

    result = os.path.join(result, "mnist", "saved", "model.ckpt-20000")

    return result
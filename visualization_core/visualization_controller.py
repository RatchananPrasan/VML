from .visualizer_mnist import MnistVisualizer
from .vis_graph import VisGraph

class VisualizationController():


    def visualize_mnist(self):
        mnist = MnistVisualizer("", VisGraph())

        result = {}

        result["data"] = mnist.get_data()
        result["dotstring"] = mnist.get_dotstring()
        result["meta"] = mnist.get_meta()

        return result

    def visualize(self, model_file_path, input_file_path):
        result = {}

        result["data"] = self._get_data()
        result["dotstring"] = self._get_dotstring()
        
        return result

    # returns dictionary with key being id of node or edges and value is its string JSON
    def _get_data(self):
        return {
            "0" : {
                    "type" : "input"
                }
            ,
            "1" : 
                {
                    "type" : "convolution",
                    "operation" : "Convolution2D",
                    "activation" : "Relu",
                    "filter_size" : {
                        "width" : 5,
                        "height" : 5
                    },
                    "filters" : [
                        [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0]
                    ],
                    "input_size" : {
                        "width" : 28,
                        "height" : 28
                    },
                    "inputs" : [
                        [0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.23137257,0,0,0,0.6392157,0,0,0,0.9960785,0,0,0,0.9960785,0,0,0,0.9960785,0,0,0,0.7607844,0,0,0,0.43921572,0,0,0,0.07058824,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.015686275,0,0,0,0.5176471,0,0,0,0.93725497,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.627451,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.5372549,0,0,0,0.9921569,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.75294125,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.8980393,0,0,0,0.050980397,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.015686275,0,0,0,0.5372549,0,0,0,0.9843138,0,0,0,0.9921569,0,0,0,0.9568628,0,0,0,0.50980395,0,0,0,0.19215688,0,0,0,0.07450981,0,0,0,0.019607844,0,0,0,0.6392157,0,0,0,0.9921569,0,0,0,0.8235295,0,0,0,0.03529412,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.37254903,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.8431373,0,0,0,0.1764706,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.6117647,0,0,0,0.9921569,0,0,0,0.68235296,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.8431373,0,0,0,0.9960785,0,0,0,0.8117648,0,0,0,0.09019608,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.039215688,0,0,0,0.3803922,0,0,0,0.85098046,0,0,0,0.9176471,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.83921576,0,0,0,0.9921569,0,0,0,0.2784314,0,0,0,0.0,0,0,0,0.0,0,0,0,0.007843138,0,0,0,0.19607845,0,0,0,0.8352942,0,0,0,0.9921569,0,0,0,0.9960785,0,0,0,0.7058824,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.83921576,0,0,0,0.9921569,0,0,0,0.19215688,0,0,0,0.0,0,0,0,0.0,0,0,0,0.19607845,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.7176471,0,0,0,0.04705883,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.7803922,0,0,0,0.9921569,0,0,0,0.95294124,0,0,0,0.7686275,0,0,0,0.62352943,0,0,0,0.95294124,0,0,0,0.9921569,0,0,0,0.9686275,0,0,0,0.5411765,0,0,0,0.03137255,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.16470589,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.39607847,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.23137257,0,0,0,0.58431375,0,0,0,0.9960785,0,0,0,0.9960785,0,0,0,0.9960785,0,0,0,1.0,0,0,0,0.9960785,0,0,0,0.6862745,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.13333334,0,0,0,0.75294125,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.7843138,0,0,0,0.53333336,0,0,0,0.89019614,0,0,0,0.9450981,0,0,0,0.27058825,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.33333334,0,0,0,0.9686275,0,0,0,0.9921569,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.77647066,0,0,0,0.48235297,0,0,0,0.07058824,0,0,0,0.0,0,0,0,0.19607845,0,0,0,0.9921569,0,0,0,0.8352942,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.2784314,0,0,0,0.9686275,0,0,0,0.9921569,0,0,0,0.9294118,0,0,0,0.75294125,0,0,0,0.2784314,0,0,0,0.023529414,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.007843138,0,0,0,0.5019608,0,0,0,0.9803922,0,0,0,0.21176472,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.46274513,0,0,0,0.9921569,0,0,0,0.8705883,0,0,0,0.14117648,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.03137255,0,0,0,0.7176471,0,0,0,0.9921569,0,0,0,0.227451,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.46274513,0,0,0,0.9960785,0,0,0,0.54509807,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.054901965,0,0,0,0.7294118,0,0,0,0.9960785,0,0,0,0.9960785,0,0,0,0.227451,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.2784314,0,0,0,0.9686275,0,0,0,0.9686275,0,0,0,0.54509807,0,0,0,0.0627451,0,0,0,0.0,0,0,0,0.0,0,0,0,0.07450981,0,0,0,0.227451,0,0,0,0.87843144,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.8313726,0,0,0,0.03529412,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.42352945,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.92549026,0,0,0,0.6862745,0,0,0,0.6862745,0,0,0,0.9686275,0,0,0,0.9921569,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.77647066,0,0,0,0.16862746,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.2627451,0,0,0,0.8352942,0,0,0,0.8980393,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.83921576,0,0,0,0.48627454,0,0,0,0.023529414,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.09019608,0,0,0,0.60784316,0,0,0,0.60784316,0,0,0,0.8745099,0,0,0,0.7843138,0,0,0,0.46274513,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0]
                    ],
                    "output_size" : {
                        "width" : 28,
                        "height" : 28
                    },
                    "outputs" : [
                        [0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.23137257,0,0,0,0.6392157,0,0,0,0.9960785,0,0,0,0.9960785,0,0,0,0.9960785,0,0,0,0.7607844,0,0,0,0.43921572,0,0,0,0.07058824,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.015686275,0,0,0,0.5176471,0,0,0,0.93725497,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.627451,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.5372549,0,0,0,0.9921569,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.75294125,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.8980393,0,0,0,0.050980397,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.015686275,0,0,0,0.5372549,0,0,0,0.9843138,0,0,0,0.9921569,0,0,0,0.9568628,0,0,0,0.50980395,0,0,0,0.19215688,0,0,0,0.07450981,0,0,0,0.019607844,0,0,0,0.6392157,0,0,0,0.9921569,0,0,0,0.8235295,0,0,0,0.03529412,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.37254903,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.8431373,0,0,0,0.1764706,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.6117647,0,0,0,0.9921569,0,0,0,0.68235296,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.8431373,0,0,0,0.9960785,0,0,0,0.8117648,0,0,0,0.09019608,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.039215688,0,0,0,0.3803922,0,0,0,0.85098046,0,0,0,0.9176471,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.83921576,0,0,0,0.9921569,0,0,0,0.2784314,0,0,0,0.0,0,0,0,0.0,0,0,0,0.007843138,0,0,0,0.19607845,0,0,0,0.8352942,0,0,0,0.9921569,0,0,0,0.9960785,0,0,0,0.7058824,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.83921576,0,0,0,0.9921569,0,0,0,0.19215688,0,0,0,0.0,0,0,0,0.0,0,0,0,0.19607845,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.7176471,0,0,0,0.04705883,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.7803922,0,0,0,0.9921569,0,0,0,0.95294124,0,0,0,0.7686275,0,0,0,0.62352943,0,0,0,0.95294124,0,0,0,0.9921569,0,0,0,0.9686275,0,0,0,0.5411765,0,0,0,0.03137255,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.16470589,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.39607847,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.23137257,0,0,0,0.58431375,0,0,0,0.9960785,0,0,0,0.9960785,0,0,0,0.9960785,0,0,0,1.0,0,0,0,0.9960785,0,0,0,0.6862745,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.13333334,0,0,0,0.75294125,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.7843138,0,0,0,0.53333336,0,0,0,0.89019614,0,0,0,0.9450981,0,0,0,0.27058825,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.33333334,0,0,0,0.9686275,0,0,0,0.9921569,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.77647066,0,0,0,0.48235297,0,0,0,0.07058824,0,0,0,0.0,0,0,0,0.19607845,0,0,0,0.9921569,0,0,0,0.8352942,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.2784314,0,0,0,0.9686275,0,0,0,0.9921569,0,0,0,0.9294118,0,0,0,0.75294125,0,0,0,0.2784314,0,0,0,0.023529414,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.007843138,0,0,0,0.5019608,0,0,0,0.9803922,0,0,0,0.21176472,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.46274513,0,0,0,0.9921569,0,0,0,0.8705883,0,0,0,0.14117648,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.03137255,0,0,0,0.7176471,0,0,0,0.9921569,0,0,0,0.227451,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.46274513,0,0,0,0.9960785,0,0,0,0.54509807,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.054901965,0,0,0,0.7294118,0,0,0,0.9960785,0,0,0,0.9960785,0,0,0,0.227451,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.2784314,0,0,0,0.9686275,0,0,0,0.9686275,0,0,0,0.54509807,0,0,0,0.0627451,0,0,0,0.0,0,0,0,0.0,0,0,0,0.07450981,0,0,0,0.227451,0,0,0,0.87843144,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.8313726,0,0,0,0.03529412,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.42352945,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.92549026,0,0,0,0.6862745,0,0,0,0.6862745,0,0,0,0.9686275,0,0,0,0.9921569,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.77647066,0,0,0,0.16862746,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.2627451,0,0,0,0.8352942,0,0,0,0.8980393,0,0,0,0.9960785,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.9921569,0,0,0,0.83921576,0,0,0,0.48627454,0,0,0,0.023529414,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.09019608,0,0,0,0.60784316,0,0,0,0.60784316,0,0,0,0.8745099,0,0,0,0.7843138,0,0,0,0.46274513,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0,0,0,0,0.0]
                    ]
                }
            ,
            "2" : 
                {
                    "type" : "convolution"
                }
            ,
            "3" : 
                {
                    "type" : "pooling"
                }
            ,
            "4" : 
                {
                    "type" : "pooling"
                }
            ,
            "5" : 
                {
                    "type" : "dense"
                }
            ,
            "6" : 
                {
                    "type" : "dense"
                }
            ,
            "7" : 
                {
                    "type" : "dense"
                }
            ,
            "8" : 
                {
                    "type" : "dense"
                }
        }

    def _get_dotstring(self):
        return """
                dinetwork {
                        0 [ level=1 ];
                        1 [ level=2 ];
                        2 [ level=2 ];
                        3 [ level=3 ];
                        4 [ level=3 ];
                        5 [ level=4 ];
                        6 [ level=4 ];
                        7 [ level=4 ];
                        8 [ level=4 ];
                        0 -- 1 [ id=e0 ];
                        0 -- 2 [ id=e1 ];
                        1 -- 3 [ id=e2 ];
                        2 -- 4 [ id=e3 ];
                        3 -- 5 [ id=e4 ];
                        3 -- 6 [ id=e5 ];
                        3 -- 7 [ id=e6 ];
                        3 -- 8 [ id=e7 ];
                        4 -- 5 [ id=e8 ];
                        4 -- 6 [ id=e9 ];
                        4 -- 7 [ id=e10 ];
                        4 -- 8 [ id=e11 ];
                      }
                """
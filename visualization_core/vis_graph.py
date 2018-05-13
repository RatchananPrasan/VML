import numpy as np

class VisGraph():

    def __init__(self):
        self.data = {}
        self.dotstring = 'dinetwork {'
        self.node_counter = 0
        self.edge_counter = 0
        self.current_level = 1
        self.prev_layers_node = []
        self.graph_meta = {
            "convolution" : [],
            "pooling" : [],
            "input" : []
        }


    def get_graph_meta(self):
        return self.graph_meta


    def get_data(self):
        return self.data


    def get_dotstring(self):
        return self.dotstring


    def end_dotstring(self):
        self.dotstring += "}"


    def draw_input(self, image, size):
        self.dotstring += str(self.node_counter) + '[label="",level=1];'

        context = {}
        context["type"] = "input"
        context["output_size"] = {}
        context["output_size"]["width"] = size[0]
        context["output_size"]["height"] = size[1]

        context["outputs"] = []
        output = []
        for i in image:
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(float(i))
        context["outputs"].append(output)

        self.data[str(self.node_counter)] = context
        self.graph_meta["input"].append([self.node_counter])

        self.prev_layers_node.append(self.node_counter)

        self.node_counter += 1
        self.current_level += 1


    def draw_convolution(self, outputs, size, kernel, kernel_size, activation):
        prev_layers = []
        all_node = []
        for i in range(outputs.shape[3]):
            self.dotstring += str(self.node_counter) + '[label="",level=' + str(self.current_level) + '];'

            for j in self.prev_layers_node:
                self.dotstring += str(j) + '--' + str(self.node_counter) + '[id=e' + str(self.edge_counter) + '];'
                self.edge_counter += 1

            context = {}
            context["type"] = "convolution"
            context["activation"] = activation

            context["filter_size"] = {}
            context["filter_size"]["width"] = kernel_size[0]
            context["filter_size"]["height"] = kernel_size[1]

            filters = []
            for k in range(kernel.shape[2]):
                rgba = []
                kernel_1d = np.reshape(kernel[:, :, k, i], (kernel_size[0] * kernel_size[1]))
                for val in kernel_1d:
                    rgba.append(0)
                    rgba.append(0)
                    rgba.append(0)
                    rgba.append(float(val))
                filters.append(rgba)

            context["filters"] = filters

            context["output_size"] = {}
            context["output_size"]["width"] = size[0]
            context["output_size"]["height"] = size[1]

            context["outputs"] = []
            output_1d = np.reshape(outputs[0, :, :, i], (size[0] * size[1]))
            result = []
            for val in output_1d:
                result.append(0)
                result.append(0)
                result.append(0)
                result.append(float(val))
            context["outputs"].append(result)
            
            context["inputs"] = self.prev_layers_node

            self.data[str(self.node_counter)] = context
            all_node.append(self.node_counter)
            
            prev_layers.append(self.node_counter)
            self.node_counter += 1

        self.graph_meta["convolution"].append(all_node)
        self.prev_layers_node = prev_layers
        self.current_level += 1
            

    def draw_pooling(self, output, size):
        prev_layers = []
        all_node = []
        for i in range(output.shape[3]):
            self.dotstring += str(self.node_counter) + '[label="",level=' + str(self.current_level) + '];'
            self.dotstring += str(self.prev_layers_node[i]) + '--' + str(self.node_counter) + "[id=e" + str(self.edge_counter) + '];'
    
            context = {}

            context["type"] = "pooling"
            context["output_size"] = {}
            context["output_size"]["width"] = size[0]
            context["output_size"]["height"] = size[1]

            context["outputs"] = []
            result = []
            output_1d = np.reshape(output[0, :, :, i], (size[0] * size[1]))
            for val in output_1d:
                result.append(0)
                result.append(0)
                result.append(0)
                result.append(float(val))
            context["outputs"].append(result)

            context["inputs"] = []
            context["inputs"].append(self.prev_layers_node[i])

            self.data[str(self.node_counter)] = context
            all_node.append(self.node_counter)
            
            prev_layers.append(self.node_counter)
            self.edge_counter += 1
            self.node_counter += 1

        self.graph_meta["pooling"].append(all_node)
        self.prev_layers_node = prev_layers
        self.current_level += 1
from django.shortcuts import render

from visualization_core.visualization_controller import VisualizationController

from visualization_core.mnist import sample
def index(request):
    
    context = {}

    controller = VisualizationController()

    information = controller.visualize("model file location", "input file location")

    context["data"] = information["data"]
    context["dotstring"] = information["dotstring"]
    size, input_data = sample.input_sample_1d()

    context["size"] = size
    context["content"] = input_data


    

    return render(request, 'visualization/index.html', context)
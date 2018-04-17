from django.shortcuts import render

from visualization_core.visualization_controller import VisualizationController

def index(request):
    context = {}

    controller = VisualizationController()

    information = controller.visualize("model file location", "input file location")

    context["data"] = information["data"]
    context["dotstring"] = information["dotstring"]

    return render(request, 'visualization/index.html', context)
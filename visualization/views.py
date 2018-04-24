from django.shortcuts import render

import json
from visualization_core.visualization_controller import VisualizationController

def index(request):
    context = {}

    controller = VisualizationController()

    information = controller.visualize_mnist()

    context["data"] = json.dumps(information["data"])
    context["dotstring"] = information["dotstring"]
    context["meta"] = information["meta"]

    return render(request, 'visualization/index.html', context)
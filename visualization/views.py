from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import json
import base64
import six
import uuid

from visualization_core.vis_graph import VisGraph
from visualization_core.visualization_controller import VisualizationController


def index(request):
    return render(request, 'visualization/index.html')


def mnist(request):
    context = {}

    controller = VisualizationController()

    information = controller.visualize_mnist()


    context["data"] = information["data"]
    context["dotstring"] = information["dotstring"]
    context["meta"] = information["meta"]

    return render(request, 'visualization/mnist.html', context)
def save_alpha(request):
    context = {}

    controller = VisualizationController()

    information = controller.visualize_mnist()


    context["data"] = information["data"]
    context["dotstring"] = information["dotstring"]
    context["meta"] = information["meta"]
    if request.method == "POST" and request.is_ajax():
        dsf = request.POST.getlist('alpha_val[]')
        print(dsf)


    return render(request, 'visualization/mnist.html', context)


def get_bas64(request):
    context = {}

    controller = VisualizationController()

    information = controller.visualize("model file location", "input file location")

    context["data"] = information["data"]
    context["dotstring"] = information["dotstring"]
    context["meta"] = information["meta"]
    if request.method == "POST" and request.is_ajax():
        # process the image
       
        image_data = request.POST['imgBase64']
        format, imgstr = image_data.split(';base64,') 
        ext = format.split('/')[-1] 
        file_name = str(uuid.uuid4())[:12]
        myfile = ContentFile(base64.b64decode(imgstr), name=file_name+'.' + ext) # You can save this as file instance.
        
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # return render(request, 'core/simple_upload.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })
        return render(request, 'visualization/mnist.html', context)
        

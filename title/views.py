from django.shortcuts import render
from encyclopedia import util
from django.http import HttpResponse
from markdown2 import Markdown
from . import customFunctions

# Create your views here.

def title(request, name):
    if customFunctions.checker(name):
        return customFunctions.render_title(request, customFunctions.checker(name))
    
    return HttpResponse(f"Page does not exist, you can create one here")




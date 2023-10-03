from django.shortcuts import render
from encyclopedia import util
from django.http import HttpResponse
from markdown2 import Markdown
from . import customFunctions
from encyclopedia import views
from django.contrib import messages

# Create your views here.

def title(request, name):
    if customFunctions.checker(name):
        return customFunctions.render_title(request, customFunctions.checker(name))
    
    messages.error(request, "The page you are requesting is not available, But You can Create one")
    return render(request, "encyclopedia/create.html",{
            "form": views.newPage(initial={'titleOfPage': name}),
            "name": name
        })




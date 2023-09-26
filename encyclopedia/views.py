from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import Markdown

from django.utils.safestring import mark_safe
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):
    name = name.upper()
    markdowner = Markdown()
    convertedInHtml = markdowner.convert(util.get_entry(name))
    if util.get_entry(name):
        return render(request, "encyclopedia/title.html", {
            "page": convertedInHtml
        })

    return HttpResponse(f"Page doesnot exist, you can create one")

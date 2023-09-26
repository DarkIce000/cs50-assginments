from django.shortcuts import render

from django.utils.safestring import mark_safe
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

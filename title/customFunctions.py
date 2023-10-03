from django.shortcuts import render
from encyclopedia import util
from markdown2 import Markdown


def render_title(request, name):
    markdowner = Markdown()
    if util.get_entry(name):
        convertedInHtml = markdowner.convert(util.get_entry(name))
        return render(request, "title/title.html", {
            "page": convertedInHtml,
            "name": name
        })


def checker(name):
    for title in util.list_entries():
        if name.lower() == title.lower():
            return title
         
    return None

def searchSequence(word, sequence):
    if sequence in word:
        return word
    return None         
import random
from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from . import util
from title import customFunctions
from django.contrib import messages

class newPage(forms.Form):
    titleOfPage = forms.CharField(label="Title")
    Description = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    name = request.POST.get("query")
    searchResult = []
    #after getting the search query page with check for the existance of page if exist it directly goes to that page
    if request.method == "POST":
        for word in util.list_entries():
            if word.lower() == name.lower().strip():
                return HttpResponseRedirect(f"/wiki/{word}")
            else:
                
                if customFunctions.searchSequence(word.lower(), name.lower().strip()):
                    searchResult.append(word)
                else:
                    continue 
        #if not it will present a page with list of search matching result 
        return render(request,"encyclopedia/search.html", {
            "searchResult": searchResult
        } )
              
#if nothing typed it will go to index page just
    return HttpResponseRedirect("/")


def create(request):
    if request.method == "POST":
        form = newPage(request.POST)
        if not customFunctions.checker(request.POST.get("titleOfPage")):
            #save title
            util.save_entry(request.POST.get("titleOfPage"), request.POST.get("Description"))
            messages.success(request, "Your Article Has Been Published!!!")
            return HttpResponseRedirect("/")
        else:
            # show error message when custom checker get some file with the title that user is currently trying to use
            # present a page with some indicating page already exist 
            messages.error(request, "Article already Exists.")
            return HttpResponse(f'There is already a page with the same title <a href="/wiki/{customFunctions.checker(request.POST.get("titleOfPage"))}/edit">Edit</a> ')
        
    return render(request, "encyclopedia/create.html", {
        "form": newPage
        })


def editPage(request, name):
    readFile = util.get_entry(customFunctions.checker(name))

    #if request of save been made after editing the page these line handle the saving logic and display a message to the user
    #on success.
    if request.method == "POST":
        util.save_entry(request.POST.get("titleOfPage"), request.POST.get("Description"))
        messages.success(request, "Congrats! Your Article Has Been Saved.")
        return HttpResponseRedirect(f"/wiki/{name}")
    
    #readFile should store the file which is already save and load the content and title 
    if readFile:
        return render(request, "encyclopedia/edit.html",{
            "form": newPage(initial={'titleOfPage': name, 'Description': readFile}),
            "name": name
        })
    
    #if somehow file cannot be opened user gets httpresponse of error in opening the file 
    return HttpResponse(f"Some Error in opening {name}.md file")



def randomize(request):
    #getting a random choice from list of availbale entries
    randomPage = random.choice(util.list_entries())
    #returning  titlePage
    return customFunctions.render_title(request, randomPage)
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .formsTemplate import formCreate, formComment, formWatchlist
from .models import User, list_item, comment, watchlist, bid, category
from django.contrib.auth.decorators import login_required
import datetime

#index page for listing all the items
def index(request):
    listItem = list_item.objects.all().exclude(active_status=False)
    return render(request, "auctions/index.html", {
        "listItem": listItem
    })


# create a list on the site
@login_required(login_url="/login")
def createListing(request):
    #getting the submitted data after the user is submitted
    if request.method == "POST":
        listing = formCreate(request.POST)

        if listing.is_valid():
            title = listing.cleaned_data["title"]
            url = listing.cleaned_data["url"]
            description = listing.cleaned_data["Description"]
            initialBid = listing.cleaned_data["initialBid"]
            ctg = listing.cleaned_data['category']

            bidding = bid(initialBid = initialBid)
            bidding.save()


            listItem = list_item(
                product_title = title,
                description=description,
                seller=request.user,
                imageUrl=url,
                bids=bidding
                )
            listItem.save()
            try:
                new_category = category.objects.get(category_title=ctg)
                new_category.product_id.add(listItem)
            except:
                new_category = category.objects.create(category_title = ctg)
                new_category.product_id.add(listItem)
                

        else:
            return render(request, "auctions/createListing.html",{
                "form": formCreate(initial={
                    "title":title,
                    "description": description,
                    "url":url,
                    "initialBid":initialBid
                    })
            })

    return render(request, "auctions/createListing.html", {
        "form": formCreate
    })


#getting the products from db
def product(request, product_id):
    try:
        product_obj = list_item.objects.get(id=product_id)
        get_comments = comment.objects.filter(product_id=product_id)
        is_in_watchlist= watchlist.objects.get(userId=request.user, product_id=product_obj) 
    except list_item.DoesNotExist:
        
        product = None
    except comment.DoesNotExist:
        get_comment = "No Comments"
    except watchlist.DoesNotExist:
        is_in_watchlist = None

    #some workaround for the js part handling and watchlist that i didnot know 
    # how to make that checkbox checked from fetching from the db 
    if is_in_watchlist :
        is_in_watchlist = "checked"
    else: 
        is_in_watchlist = "unchecked"

    #if the seller is the logged in user display close button else display bidding form 
    is_user = ""
    if request.user == product_obj.seller:
        is_user = True

    return render(request, "auctions/productPage.html",{
        "product_info": product_obj,
        "add_watchlist": formWatchlist(),
        "formComment":formComment(),
        "display_comments": get_comments, 
        "is_in_watchlist": is_in_watchlist,
        "is_user": is_user
    })


#commenting feature onthe product page
def commentMade(request, product_id):
    commentobj = formComment(request.POST)
    get_product = list_item.objects.get(id = product_id)
    if request.method == "POST":
        if commentobj.is_valid():
            comment_title = commentobj.cleaned_data['title']
            comment_msg = commentobj.cleaned_data["msg"]

			#saving to the comment table
            comment_save = comment(title=comment_title, msg=comment_msg, product_id=get_product)
            comment_save.save()
            return HttpResponseRedirect(reverse("product_page",args=(product_id,)))

        return HttpResponseRedirect(reverse("product_page", args=(product_id,)), {
            "message" : "comment is invalid"
            })

    return HttpResponseRedirect(reverse("index"))


#watchlist implementation
@login_required(login_url="/login")
def watchlist_view(request, product_id=0):

    if request.method == "POST":
        # if marked in watchlist checkbox then add to the db
        try:     
            product_obj = list_item.objects.get(id=product_id)
            try:
                watchlist_obj = watchlist.objects.get(userId=request.user, product_id=product_obj)
            except:
                watchlist_obj = None
        except:
            return HttpResponse(f' Bad Request')

        if(request.POST.get('addToWatchlist') and not watchlist_obj):
            add_to_watchlist = watchlist(userId=request.user, product_id=product_obj)
            add_to_watchlist.save()
        #if exits and unchecked then  remove 
        elif(not request.POST.get('addToWatchlist') and watchlist_obj):
            watchlist_obj.delete() 

        return HttpResponseRedirect(reverse("product_page", args=(product_id,)))

    get_watchlist_for_user = watchlist.objects.filter(userId=request.user)
    return render(request, "auctions/watchlist.html", {"list": get_watchlist_for_user})


@login_required(login_url='/login')
def bidding_view(request, product_id=0):
    if request.method == "POST":
        try: 
            get_product = list_item.objects.get(id=product_id)                
        except:
            get_product = None 

        if request.POST.get("closeButton"):
            # last time check if the user is the seller then change status to close and redirect to the product page 
            if request.user == get_product.seller :
                get_product.active_status = False 
                get_product.save()

                return HttpResponseRedirect(reverse('index'))

        if request.POST.get("biddingField"): 
            if (int(request.POST.get("biddingField")) > int(get_product.bids.last_bid)):
                #update the last bidding if they make the greater than the last bidding
                get_product.bids.last_bid = request.POST.get('biddingField')
                get_product.bids.last_bidder = request.user

                get_product.bids.save()

                return HttpResponseRedirect(reverse('product_page', args=(product_id, )))
            else: 
                return HttpResponseRedirect(reverse('product_page', args=(product_id, )))

    try:
        won_bids = list_item.objects.filter(bids__last_bidder=request.user).filter(active_status=False)
    except:
        won_bids = None 

    try:
        current_bids = list_item.objects.filter(bids__last_bidder=request.user).exclude(active_status=False)
    except:
        current_bids = None

    return render(request, "auctions/my-bids.html", {"won_bids": won_bids, "current_bids": current_bids})
            

def categories_view(request):
    try:
        categories = category.objects.values('category_title').distinct()
        return render(request, "auctions/categories.html", {"ctg": categories})
    except:
        return render(request,"auctions/categories.html", {"ctg": None})

def category_item_list(request, category_name):
    list_of_items_in_category = category.objects.get(category_title=category_name)
    item_inthe_category = list_of_items_in_category.product_id.all()

    return render (request, "auctions/category_items.html", {
        "category_name": category_name,
        "item_inthe_category": item_inthe_category
    })


@login_required(login_url='/login')
def my_listing(request):
    try:
        users_listing = list_item.objects.filter(seller=request.user).filter(active_status=True)
    except:
        users_listing = None 
    return render(request, "auctions/my-listing.html", {
        "list": users_listing
    })





    
















def login_view(request):

    next = ""
    if request.GET:
        next = request.GET['next']

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            if next is not "":
                return HttpResponseRedirect(next)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html", {
            "next" : next
        })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

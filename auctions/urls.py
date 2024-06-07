from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createListing, name="createListing"),
    path("mybids", views.bidding_view, name="bidding_view"),
    path("categories", views.categories_view, name="categories_view"),
    path("categories/<str:category_name>", views.category_item_list, name="category_item_list"),
    path("watchlistPage/", views.watchlist_view, name="watchlistPage_view" ),
    path("<int:product_id>", views.product, name="product_page"),
    path("<int:product_id>/bidding", views.bidding_view, name="bidding_view"),
    path("<int:product_id>/watchlist", views.watchlist_view, name="add_to_watchlist"),
    path("<int:product_id>/commentMade", views.commentMade, name="commentMade"),
    path("mylisting/", views.my_listing, name="my_listing")
]

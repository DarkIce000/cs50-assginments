from django.urls import path

from . import views

app_name = "homepage"
urlpatterns = [
    path("", views.index, name="index"),
    path("s/", views.search, name="search"),
    path("create/", views.create, name="create" ),
    path('randomize/', views.randomize, name="randomize"),
    path("wiki/<str:name>/edit/", views.editPage, name="edit"),

]
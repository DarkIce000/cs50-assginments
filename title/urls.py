from django.urls import path
from . import views

app_name="title"
urlpatterns =[
    path("<str:name>", views.title, name="title")
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("group/", views.group_list, name="group_list"),
    path("group/<slug:slug>", views.group_posts, name="group_posts")
]

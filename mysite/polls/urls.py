from django.urls import path

from . import views

urlpatterns = [
    path("",views.Index.as_view(), name="Index"),
    path("playlist/",views.List.as_view(), name="List"),
]
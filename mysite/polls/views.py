from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = "index.html"

class List(TemplateView):
    template_name = "list.html"

#class Index(TemplateView):
#    template_name = "playlist.html"
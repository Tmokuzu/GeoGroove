from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = "test.html"

#class Index(TemplateView):
#    template_name = "map.html"

#class Index(TemplateView):
#    template_name = "playlist.html"
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Music
# Create your views here.

class Index(TemplateView):
    template_name = "index.html"

class List(TemplateView):
    template_name = "test2.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["Musics"] = Music.objects.all
        return context
    #for M in Musics:
    #print(Musics)

#class Index(TemplateView):
#    template_name = "playlist.html"
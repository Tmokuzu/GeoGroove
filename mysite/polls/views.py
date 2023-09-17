from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import requests

# Create your views here.

class Index(TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        selectedArea = request.POST.get('area', '')

        response = requests.post('http://backend_url_here', data={'area': selectedArea})
        
        if response.status_code == 200:
            tunes_data = response.json()
            return render(request, 'list.html', {'tunes_data': tunes_data})
        else:
            return HttpResponse('リクエストが失敗しました。')

class List(TemplateView):
    template_name = "list.html"

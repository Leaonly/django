from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    html = '新闻频道首页'
    #return HttpResponse(html)
    return render(request, 'news/index.html')
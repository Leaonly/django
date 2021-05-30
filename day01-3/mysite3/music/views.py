from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    html = '音乐频道首页'
    return HttpResponse(html)
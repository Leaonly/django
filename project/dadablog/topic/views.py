from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from tools.logging_dec import logging_check

# 异常码 10300-10399

# Create your views here.
class TopicViews(View):

    @method_decorator(logging_check)
    def post(self, request,author_id):

        author = request.myuser
        # 取出前端数据
        # 创建topic数据

        return JsonResponse({'code':200})
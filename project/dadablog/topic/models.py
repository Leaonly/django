from django.db import models
from user.models import UserProfile

# Create your models here.
# 1.文章内容，后端给前端全部内容自己截取
# 2.后端从数据库获取全部文章内容，截取后响应给前端
# 3.数据库冗余一个简介字段，后端只取简介字段内容

class Topic(models.Model):

    title = models.CharField(max_length=50, verbose_name='文章标题')
    category = models.CharField(max_length=20, verbose_name='文章分类')
    limit = models.CharField(max_length=20, verbose_name='文章权限')
    introduce = models.CharField(max_length=90, verbose_name='文章简介')
    content = models.TextField(verbose_name='文章内容')
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
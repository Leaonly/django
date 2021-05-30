from django.db import models
from django.db.models.base import Model

# Create your models here.
class Publisher(models.Model):

    name = models.CharField('出版社名称', max_length=50)

class Book(models.Model):

    title = models.CharField('书名', max_length=11)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


    
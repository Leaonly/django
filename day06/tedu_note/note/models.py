from django.db import models
from user.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField('是否活跃', default=True)

    class Meta:
        # db_table = 'note'
        verbose_name = '笔记'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s_%s_%s' % (self.title, self.content, self.is_active)
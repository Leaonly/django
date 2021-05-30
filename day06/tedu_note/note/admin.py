from django.contrib import admin
from .models import Note

# Register your models here.
class NoteManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['id', 'title', 'content','create_time', 'update_time', 'user_id', 'is_active']
    # 链接到修改页
    list_display_links = ['title']
    # 添加搜索框
    search_fields = ['title', 'content']



admin.site.register(Note, NoteManager)
from django.contrib import admin
from .models import Book, Author

class BookManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['id', 'title', 'pub', 'price', 'market_price', 'is_active']
    # 链接到修改页
    list_display_links = ['title']
    # 添加过滤器
    list_filter = ['pub']
    # 添加搜索框
    search_fields = ['title']
    # 添加编辑列表页字段
    list_editable = ['price']
    
class AuthorManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
    list_display_links = ['name']

# Register your models here.
admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)


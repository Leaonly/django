from django.contrib import admin
from .models import User

# Register your models here.
class UserManager(admin.ModelAdmin):
    list_display = ['id', 'username', 'create_time', 'update_time']
    list_display_links = ['username']

admin.site.register(User, UserManager)

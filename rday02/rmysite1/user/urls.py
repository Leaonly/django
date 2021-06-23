from . import views
from django.urls import path

urlpatterns = [
    path('detail/<int:user_id>', views.user_detail),
    path('update', views.user_update)
]
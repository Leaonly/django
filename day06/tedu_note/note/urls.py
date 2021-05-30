from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('all', views.list_view),
    path('add', views.add_note),
    path('update/<int:note_id>', views.update_note),
    path('page', views.page_note),
    path('delete', views.del_note),
]
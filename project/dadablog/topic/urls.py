from . import views
from django.urls import path

urlpatterns = [
    path('<str:author_id>', views.TopicViews.as_view())
]
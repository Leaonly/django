from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('regs', views.reg_view),
    path('login', views.login_view),
    path('logout', views.logout_view),
]
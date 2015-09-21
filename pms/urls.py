__author__ = 'William'

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^',views.index, name='index'),
    url(r'^login_test/',views.loginTest, name='loginTest'),
    url(r'^profile/',views.setupProfile, name='setupProfile'),
]

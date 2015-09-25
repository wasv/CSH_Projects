__author__ = 'William'

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^login_test/',views.loginTest, name='loginTest'),
    url(r'^profile/edit/',views.setupProfile, name='setupProfile'),
    url(r'^project/new/',views.newProject, name='newProject'),
    url(r'^',views.index, name='index'),
]

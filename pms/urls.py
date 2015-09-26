__author__ = 'William'

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^login_test/$', views.loginTest, name='loginTest'),
    url(r'^profile/edit/$', views.profileCreate, name='profileCreate'),
    url(r'^profile/view/(?P<uname>\w+)/', views.profileView, name='profileView'),
    url(r'^project/new/$', views.projectCreate, name='projectCreate'),
    url(r'^project/edit/(?P<project_id>[0-9]+)/', views.projectEdit, name='projectEdit'),
    url(r'^project/view/(?P<project_id>[0-9]+)/', views.projectDetail, name='projectDetail'),
    url(r'^$', views.index, name='index'),
]

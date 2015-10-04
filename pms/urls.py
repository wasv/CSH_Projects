__author__ = 'William'

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^login_test/$', views.loginTest, name='loginTest'),
    url(r'^editprofile/$', views.profileCreate, name='profileCreate'),
    url(r'^profile/(?P<uname>\w+)/', views.profileView, name='profileView'),
    url(r'^project/new/$', views.projectCreate, name='projectCreate'),
    url(r'^project/edit/(?P<project_id>[0-9]+)/', views.projectEdit, name='projectEdit'),
    url(r'^project/view/(?P<project_id>[0-9]+)/', views.projectView, name='projectView'),
    url(r'^list/active/', views.listActive, name='listActive'),
    url(r'^list/all/', views.listAll, name='listAll'),
    url(r'^list/dead/', views.listDead, name='listDead'),
    url(r'^list/done/', views.listDone, name='listDone'),
    url(r'^$', views.index, name='index'),
]

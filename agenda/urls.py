from django.conf.urls import url
from .views import hello_world

urlpatterns = [
    #...,

    url(r'^hello-world/$', hello_world, name='hello-world
    url(r'^hello-world/$', hello_world, name='hello-world'),'),]

from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'posts', include("posts.urls")),
    url(r'profile', views.profile, name='profile'),
    url(r'staffprofile', views.staffprofile, name='staffprofile'),
    url('access', views.access, name='access'),
    url(r'^$', views.home, name='home')
]
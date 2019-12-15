from django.contrib import admin
from django.conf.urls import url, include
from . import views
from posts import views as post_view
from Profile import views as profView

urlpatterns = [
    url(r'^posts', include("posts.urls")),
    url(r'^profile', profView.profile, name='profile'),
    url(r'^$', views.home, name='home')
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'details/(?P<id>\d+)$', views.details, name='details'),
    url(r'posts/', views.index, name='index'),
    url(r'^$', views.index, name='index')
]
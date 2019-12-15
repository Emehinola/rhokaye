from django.conf.urls import url
from . import views

urlpatterns = [
    url('^', views.access, name='access'),
    url('^profile', views.profile, name='profile')
]

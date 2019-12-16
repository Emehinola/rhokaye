from django.conf.urls import url
from . import views

urlpatterns = [
    url('vacancy/applications', views.application, name='application'),
    url('', views.vacancy, name='vacancy')
]

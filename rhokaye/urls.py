"""School_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from vacancy import views as vac_views
from posts import views as post_views


urlpatterns = [
    url(r"admin/", admin.site.urls),
    
    url(r'login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'logout/', auth_view.LogoutView.as_view(template_name='users/home.html'), name='logout'),
    url(r'login/', user_views.login, name='login'),
    url(r'^register', user_views.register, name='register'),
    url(r'home/', user_views.home, name='home'),
    url(r'posts/', include('posts.urls')),
    url('application', vac_views.application, name='application'),
    url('announcement', post_views.announcement, name='announcement'),
    url(r'vacancy', include('vacancy.urls')),
    url(r'^', include('users.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
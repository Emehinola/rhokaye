from django.contrib import admin
from .models import Posts
from .models import Comments
# Register your models here.

admin.site.register(Posts)

admin.site.register(Comments)
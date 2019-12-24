from django.contrib import admin
from .models import Posts
from .models import Comments, Announcement, Enquiry
# Register your models here.

admin.site.register(Posts)

admin.site.register(Comments)

admin.site.register(Announcement)

admin.site.register(Enquiry)
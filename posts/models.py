from django.db import models
from datetime import datetime
import django.utils.timezone

# Create your models here.
class Posts(models.Model):

    title = models.CharField(max_length=200)

    body = models.TextField()

    image = models.FileField(null=True,upload_to='posts_pics')

    created_at = models.DateField(default=datetime.now, blank=False)

    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

class Comments(models.Model):
    post_comment = models.ForeignKey("Posts", on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
    
    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ['-created']

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    by = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Announcement'
        ordering = ['-time']

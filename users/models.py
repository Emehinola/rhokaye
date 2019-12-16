from django.db import models
from django.contrib.auth.models import User

class  Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='', upload_to='posts_pics')
    email = models.EmailField(default="")
    state = models.CharField(default="",max_length=15)
    nationality = models.CharField(default="",max_length=15)
    address = models.CharField(default="",max_length=50)
    religion = models.CharField(default="",max_length=10)

    def __str__(self):
        return f"{self.user.username} Profile"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
from django.db import models
from django.contrib.auth.models import User

class  Profile(models.Model):

    # students details
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='', upload_to='posts_pics')
    state = models.CharField(default="",max_length=15)
    nationality = models.CharField(default="",max_length=15)
    address = models.CharField(default="",max_length=50)
    religion = models.CharField(default="",max_length=20)
    category = models.CharField(default="",max_length=30)
    Class = models.CharField(default="",max_length=10)
    department = models.CharField(default="",max_length=30)
    post = models.CharField(default="",max_length=10)

    # parent details
    parent_name = models.CharField(default="",max_length=40)
    parent_number = models.CharField(default="",max_length=14)
    parent_address = models.CharField(default="",max_length=50)
    occupation = models.CharField(default="",max_length=50)

    def __str__(self):
        return f"{self.user.username} Profile"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class  StaffProfile(models.Model):

    # staff details
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='media/download.jpg', upload_to="profile_pix")
    state = models.CharField(default="",max_length=15)
    nationality = models.CharField(default="",max_length=15)
    address = models.CharField(default="",max_length=50)
    religion = models.CharField(default="",max_length=20)
    category = models.CharField(default="",max_length=30)
    post = models.CharField(default="",max_length=10)
    department = models.CharField(default="",max_length=30)
    phone = models.CharField(default="",max_length=255)
    Payment_status = models.CharField(default="",max_length=50)
    date_joined = models.CharField(default="",max_length=30)


    def __str__(self):
        return f"{self.user.username} Profile"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
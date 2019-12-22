from django.db import models

class Vacancy(models.Model):
    job_title = models.CharField(default="",max_length=100)
    post = models.CharField(max_length=100)
    qualifications = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    salary = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    requirements = models.CharField(max_length=300)
    job_description = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.job_title
    
    class Meta:
        verbose_name_plural = 'Vacancy'
        ordering = ['-created_at']

class Applications(models.Model):

    vacancy = models.ForeignKey(Vacancy,default="", on_delete="")
    first_name = models.CharField(default="",max_length=20)
    last_name = models.CharField(default="",max_length=30)
    post = models.CharField(max_length=100)
    qualifications = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    phone = models.CharField(default="",max_length=20)
    years_of_experience = models.IntegerField()
    location = models.CharField(max_length=200)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name_plural = 'Applications'
        ordering = ['-created_at']

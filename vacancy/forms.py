from django import forms
from django.db import models
from .models import Vacancy, Applications


class Application(forms.ModelForm):
    vacancy = models.ForeignKey(Vacancy, on_delete="")
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    post = forms.CharField(max_length=100)
    qualifications = forms.CharField(max_length=100)
    email_address = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    years_of_experience = forms.IntegerField()
    location = forms.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)


    class Meta:

        model = Applications
        fields = ['first_name', 'last_name', 'vacancy', 'post', 'email', 'phone', 'qualifications', 'years_of_experience', 'location']

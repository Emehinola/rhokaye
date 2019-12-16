from django import forms
from .models import Comments, Posts
from django.db import models

class CommentForm(forms.ModelForm):
    author = forms.CharField(max_length=20)
    body = forms.Textarea()
 
    class Meta:

        model = Comments
        fields = ['author', 'body']

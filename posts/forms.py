from django import forms
from .models import Comments, Posts, Enquiry
from django.db import models

class CommentForm(forms.ModelForm):
    author = forms.CharField(max_length=20)
    body = forms.Textarea()
 
    class Meta:

        model = Comments
        fields = ['author', 'body']

class EnquiryForm(forms.ModelForm):
    Email = forms.EmailField()
    phone = forms.CharField()
    classes_to_enrol = forms.CharField()
 
    class Meta:

        model = Enquiry
        fields = ['Email', 'phone','classes_to_enrol']
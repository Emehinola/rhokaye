from django import forms
from .models import Comments, Posts
from django.db import models

class CommentForm(forms.ModelForm):
    user = models.CharField(max_length=20)
    post_comment = models.ForeignKey("Posts", on_delete=models.CASCADE)
    body = forms.Textarea()

    def form_valid(self, form):
        form.instance.post_comment_id = 8
 
    class Meta:

        model = Comments
        fields = ['user', 'post_comment', 'body']

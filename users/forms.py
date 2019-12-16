from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your models here.
class UserForm(UserCreationForm):
    username = forms.CharField(max_length=15)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()


    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']
        exclude = ['password1.help_text', 'password2.help_text']

class UserLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active for now, contact the admin if you are the owner of this account')
        
        return super(UserLogin, self).clean(*args, **kwargs)
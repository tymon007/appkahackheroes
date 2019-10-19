from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    howManyPeople = forms.IntegerField(help_text="HAhaha")

    class Meta:
        model = User
        fields = ('username', 'email', 'howManyPeople', 'password1', 'password2', )

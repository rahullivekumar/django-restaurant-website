from django import forms
from .models import *
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    name=forms.CharField(label="enter first name",max_length=50)
    lastname=forms.CharField(label="eter last name", max_length=50)


class userform(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),required=True,max_length=50)

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
                               required=True, max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password again'}),
        required=True, max_length=50)

    class Meta():
        model=User
        fields=['username','password']



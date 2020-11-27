
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    pais=forms.CharField()
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    provincia=forms.CharField(max_length=200)
    celular=forms.IntegerField()
   
    
  
    class Meta:
        model=User
        fields=['pais','provincia','celular','username','email','first_name','last_name','password1','password2']
        help_texts= {k:" " for k in fields }
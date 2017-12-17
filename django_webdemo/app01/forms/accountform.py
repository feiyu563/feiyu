#coding=utf8
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=3)
    password=forms.CharField(min_length=5)
    email=forms.EmailField()
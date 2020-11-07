
from django import forms


class InputForm(forms.Form):
    email = forms.CharField(max_length=200,widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
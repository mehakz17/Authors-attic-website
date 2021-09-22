from django import forms
from .models import *


class RequestForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    Author = forms.CharField(max_length=50)
    booktitle = forms.CharField(max_length=50)
    Genre = forms.CharField(max_length=50)
    information = forms.CharField(max_length=69)

    def __str__(self):
        return self.name
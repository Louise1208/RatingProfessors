from django import forms
from .models import Rate

"""
forms used to store
"""
class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('course', 'rate')

from django.forms import widgets
class UserForm(forms.Form):
    user = forms.CharField(max_length=200,
                           label='user name',
                           widget=widgets.TextInput(attrs={'class': 'form-control'})
                           )
    pwd = forms.CharField(max_length=32,
                          label='password',
                          widget=widgets.PasswordInput(attrs={'class': 'form-control'})
                          )
    re_pwd = forms.CharField(max_length=32,
                             label='repeat password',
                             widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=32,
                             label='email',
                             widget=widgets.EmailInput(attrs={'class': 'form-control'}))
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    address = forms.CharField(max_length=255, required=True)
    verified = forms.BooleanField(required=False, initial=False, help_text="Are you verified?")
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username
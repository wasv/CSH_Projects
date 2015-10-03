from django import forms
from django.contrib.auth.models import User
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','website','picture']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','state','website','documentation']
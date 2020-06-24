from django import forms
from .models import student,UserProfileInfo
from django.contrib.auth.models import User

class NewStudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = student
        fields = '__all__'

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        files = ('portfolio_site','profile_pic')
        exclude = ()

from django import forms
from .models import student

class NewStudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = student
        fields = '__all__'

from django import forms
from .models import Lawyer

from django.core.validators import RegexValidator

class LawyerForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit phone number')]
    )
    class Meta:
        model = Lawyer
        fields = ['name' , 'img','doc','phone','specialization' ,'bio','location']
    
""""
class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title','description']

class Replyform(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['message']"""

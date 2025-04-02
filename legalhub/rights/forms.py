from django import forms
from .models import Lawyer, Case, Client
from django.core.validators import RegexValidator

class LawyerForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit phone number')]
    )

    supervising_lawyer = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Supervising Lawyer (Enter Name)"
    )

    associated_lawyers = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        label="Associated Lawyers (Enter Names, comma-separated)"
    )

    class Meta:
        model = Lawyer
        fields = ['name', 'img', 'doc', 'phone', 'specialization', 'bio', 'location', 'associated_lawyers', 'supervising_lawyer']

class CaseForm(forms.ModelForm):
    client_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter client name'}),
        label="Client Name"
    )

    case_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter case name'}),
        label="Case Name"
    )

    completion = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter completion %'}),
        label="Completion Percentage"
    )

    class Meta:
        model = Case
        fields = ['client_name', 'case_name', 'completion']
from django import forms
from .models import Job
class SearchForm(forms.Form):
    EXPERIENCES = [('', 'All experiences')] + Job.EXPERIENCES
    TYPES = [('', 'All types')] + Job.TYPES
    key_word = forms.CharField(
        max_length=200, 
        required=False, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-right',
                'placeholder': 'Skills, Designation, Companies',
                'id': "key_words",
            }
        )
    )
    experience = forms.CharField(
        max_length=200, 
        required=False, 
        widget=forms.Select(
            attrs={
                'class': 'selectpicker border-right',
                'placeholder': 'Skills, Designation, Companies',
                'id': "key_words",
            }, 
            choices=EXPERIENCES
        )
    )
    category = forms.CharField(
        max_length=200, 
        required=False, 
        widget=forms.Select(
            attrs={
                'class': 'selectpicker border-right',
                'placeholder': 'Skills, Designation, Companies',
                'id': "key_words",
            },
            choices=TYPES
        )
    )
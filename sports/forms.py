from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        exclude = ['host']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Event Name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'date_time': forms.TextInput(attrs={'placeholder': 'Date & Time'}),
            'details': forms.Textarea(attrs={'placeholder': 'Event Details'}),
        }

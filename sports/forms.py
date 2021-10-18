from django import forms
from .models import Match

class MatchForm2(forms.ModelForm):
    class Meta:
        model = Match
        exclude = ['host']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Event Name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'date_time': forms.TextInput(attrs={'placeholder': 'Date & Time'}),
            'details': forms.Textarea(attrs={'placeholder': 'Event Details'}),
        }

class MatchForm(forms.Form):
    event_name = forms.CharField(label='Event Name', widget=forms.TextInput(attrs={'placeholder': 'Event Name'}))
    event_location = forms.CharField(label='Location', widget=forms.TextInput(attrs={'placeholder': 'Location'}))
    event_date = forms.DateField(label='Date', widget=forms.TextInput(attrs={'placeholder': 'Date', 'type': 'date'}))
    event_time = forms.TimeField(label='Time', widget=forms.TextInput(attrs={'placeholder': 'Time', 'type': 'time'}))
    event_details = forms.CharField(label='Event Details', widget=forms.Textarea(attrs={'rows': '6'}))

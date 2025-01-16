from django import forms
from .models import Booking
from datetime import datetime
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django import forms
from .models import Booking

from django import forms
from .models import Booking

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'start_time', 'end_time', 'user']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'user': forms.TextInput(attrs={'readonly': 'readonly'})  # Make the user field readonly
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Extract the user from the keyword arguments
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user.username  # Set the current user's username as the initial value for the 'user' field

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Invalid username or password.')

        return cleaned_data
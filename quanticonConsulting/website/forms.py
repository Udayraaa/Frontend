from datetime import datetime

from django import forms
from django.utils.translation import gettext_lazy as _



class ContactForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    email_from = forms.EmailField(required=True, label="Enter Email")
    subject = forms.CharField(required=True)
    phone_number = forms.CharField(max_length=17, label="Your phone number")
    message = forms.CharField(widget=forms.Textarea, required=True)
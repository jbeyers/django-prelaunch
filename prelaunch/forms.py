import hashlib
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext

from django.conf import settings
from settings import *
from models import PrelaunchSubscriber
from shorten import ShortCode


class PrelaunchForm(forms.Form):          
    email_address = forms.EmailField()
    prelaunch_referrer = forms.CharField(
        widget=forms.HiddenInput(),
        required=False)


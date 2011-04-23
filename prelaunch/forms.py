import hashlib
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext

from django.conf import settings
from settings import *


class ContactForm(forms.Form):
    email_address = forms.EmailField()
    prelaunch_referrer = forms.CharField(widget=forms.HiddenInput(), required=False)

def prelaunch(request):
    prelaunch_parameter = getattr(settings,
                                  'PRELAUNCH_PARAMETER_NAME',
                                  PRELAUNCH_PARAMETER_NAME)
    print prelaunch_parameter
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            c = Context({
                'email_address': form.cleaned_data['email_address'],
                'referrer_parameter': prelaunch_parameter,
                'referrer_code': form.cleaned_data['prelaunch_referrer'],
            })
            subject = loader.get_template('prelaunch/confirmation_email_subject.txt').render(c)
            # Ensure that we have a single line subject
            subject = subject.split('\n')[0]
            message = loader.get_template('prelaunch/confirmation_email.txt').render(c)
            email_address = form.cleaned_data['email_address']
            sender = ''
            if settings.ADMINS:
                sender = settings.ADMINS[0][1]
            recipients = [i[1] for i in settings.ADMINS]
            recipients.append(email_address)
            send_mail(subject, message, sender, recipients)

    else:
        prelaunch_referrer = request.COOKIES.get('prelaunch_referrer', '')
        if not prelaunch_referrer and request.REQUEST.get(prelaunch_parameter, ''):
            prelaunch_referrer = request.REQUEST.get(prelaunch_parameter, '')
        form = ContactForm(initial={'prelaunch_referrer': prelaunch_referrer})

    return render_to_response('prelaunch/prelaunch.html', {
        'form': form,
    }, context_instance=RequestContext(request))

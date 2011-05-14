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

def prelaunch(request):
    """ Handle the prelaunch form and user generation.
    """
    prelaunch_parameter = getattr(settings,
                                  'PRELAUNCH_PARAMETER_NAME',
                                  PRELAUNCH_PARAMETER_NAME)

    prelaunch_offset = getattr(settings, 'PRELAUNCH_OFFSET', PRELAUNCH_OFFSET)
    prelaunch_digits = getattr(settings, 'PRELAUNCH_DIGITS', PRELAUNCH_DIGITS)
    shortcode = ShortCode(prelaunch_offset, prelaunch_digits)

    if request.method == 'POST': # If the form has been submitted...
        form = PrelaunchForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            referrer = None
            if form.cleaned_data['prelaunch_referrer']:
                referrer_id = shortcode.get_number(form.cleaned_data['prelaunch_referrer'])
                if referrer_id:
                    referrer = PrelaunchSubscriber.objects.filter(id=referrer_id)
                    if referrer:
                        referrer = referrer[0]

            # Create a prelaunch user, if needed.
            subscriber = PrelaunchSubscriber.objects.filter(email=form.cleaned_data['email_address'])
            if not subscriber:
                subscriber = PrelaunchSubscriber(email=form.cleaned_data['email_address'], referrer=referrer)
                subscriber.save()
            else:
                subscriber = subscriber[0]


            # Send a welcoming/explanatory email
            c = Context({
                'http_referer': request.META['HTTP_REFERER'],
                'email_address': form.cleaned_data['email_address'],
                'referrer_parameter': prelaunch_parameter,
                'referrer_code': subscriber.shortcode,
            })

            # Ensure that we have a single line subject, since templates add a
            # linefeed automatically.
            subject = loader.get_template(
                      'prelaunch/confirmation_email_subject.txt').render(c)
            subject = subject.split('\n')[0]

            message = loader.get_template(
                      'prelaunch/confirmation_email.txt').render(c)
            email_address = form.cleaned_data['email_address']
            sender = ''
            if settings.ADMINS:
                sender = settings.ADMINS[0][1]
            recipients = [i[1] for i in settings.ADMINS]
            recipients.append(email_address)

            send_mail(subject, message, sender, recipients)

    else:
        prelaunch_referrer = request.COOKIES.get('prelaunch_referrer', '')
        if not prelaunch_referrer \
            and request.REQUEST.get(prelaunch_parameter, ''):
            prelaunch_referrer = request.REQUEST.get(prelaunch_parameter, '')
        form = PrelaunchForm(initial={'prelaunch_referrer': prelaunch_referrer})

    return render_to_response(
        'prelaunch/prelaunch.html',
        {'form': form},
        context_instance=RequestContext(request))

from django import template
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader, Context

from prelaunch.settings import *
from prelaunch.models import PrelaunchSubscriber
from prelaunch.shorten import ShortCode
from prelaunch.forms import PrelaunchForm

register = template.Library()

@register.inclusion_tag('prelaunch/inclusion_tags/prelaunch_form.html', takes_context=True)
def prelaunch_form(context):
    """
    The prelaunch form.
    """
    request = context['request']
    prelaunch_parameter = getattr(settings,
                                  'PRELAUNCH_PARAMETER_NAME',
                                  PRELAUNCH_PARAMETER_NAME)

    prelaunch_offset = getattr(settings, 'PRELAUNCH_OFFSET', PRELAUNCH_OFFSET)
    prelaunch_digits = getattr(settings, 'PRELAUNCH_DIGITS', PRELAUNCH_DIGITS)
    shortcode = ShortCode(prelaunch_offset, prelaunch_digits)
    email_hash = ''

    if request.method == 'POST': # If the form has been submitted...
        form = PrelaunchForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            referrer = None
            if form.cleaned_data['prelaunch_referrer']:
                referrer_id = shortcode.get_number(
                              form.cleaned_data['prelaunch_referrer'])
                if referrer_id:
                    referrer = PrelaunchSubscriber.objects.filter(
                               id=referrer_id)
                    if referrer:
                        referrer = referrer[0]

            # Create a prelaunch user, if needed.
            subscriber = PrelaunchSubscriber.objects.filter(
                         email=form.cleaned_data['email_address'])
            if not subscriber:
                subscriber = PrelaunchSubscriber(
                             email=form.cleaned_data['email_address'],
                             referrer=referrer)
                subscriber.save()
            else:
                subscriber = subscriber[0]


            email_hash = '%s?%s=%s' % (request.META['HTTP_REFERER'],
                                       prelaunch_parameter,
                                       subscriber.shortcode)
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

    return {'form_target': request.path,
            'email_hash': email_hash,
            'form': form}


import hashlib
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext

hashtard = '1245lnaghbowe5opiumw45kjldfiujl'

class ContactForm(forms.Form):
    sender = forms.EmailField()

def prelaunch(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            ref_code = ''
            ref_url = ''
            c = Context({
                'email_address': form.cleaned_data['sender'],
                'ref_code': ref_code,
                'ref_url': ref_url,
            })
            subject = 'Clouditto early beta request'
            message = 'Please please can I join?'
            sender = form.cleaned_data['sender']
            recipients = ['info@clouditto.com']
            recipients.append(sender)
            email_hash = 'http://clouditto.com/r/'+hashtard

            send_mail(subject, message, 'info@clouditto.com', recipients)

    else:
        form = ContactForm() # An unbound form

    return render_to_response('prelaunch/prelaunch.html', {
        'form': form,
        'email_hash': email_hash
    }, context_instance=RequestContext(request))

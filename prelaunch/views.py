from django.shortcuts import render_to_response

def referrer(request, referrer):
    response = HttpResponseRedirect('/')
    if not request.get_cookie('prelaunch_referrer'):
        response.set_cookie('prelaunch_referrer', referrer)
    return response

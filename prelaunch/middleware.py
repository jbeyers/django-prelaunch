from django.conf import settings
from settings import *

class PrelaunchMiddleware(object):
    """ Adds a cookie to the response if a referrer parameter is present.
    """

    def process_response(self, request, response):
        """ Add or change the cookie.
        """
        prelaunch_parameter = getattr(settings,
                                      'PRELAUNCH_PARAMETER_NAME',
                                      PRELAUNCH_PARAMETER_NAME)

        referrer = request.REQUEST.get(prelaunch_parameter, None)
        if referrer and not request.COOKIES.get('prelaunch_referrer'):
            response.set_cookie('prelaunch_referrer', referrer)
        return response

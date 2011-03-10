from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from shorten import ShortCode

class PrelaunchSubscriber(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField()

    @property
    def shortcode(self):
        """ Get a shortcode for the user """
        shortcoder = ShortCode(settings.PRELAUNCH_OFFSET, PRELAUNCH_DIGITS)
        return shortcoder(self.id)


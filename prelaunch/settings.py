# The following settings are the defaults. If you want to override them, you
# can copy them to your main settings.py and adjust as needed.

# The numbers and letters allowed in the referral code. A string, with no
# repeats. The string below consists of numbers and lower-case letters, with 0,
# o, 1, i and l removed to make it easier to copy by hand without confusion.
PRELAUNCH_DIGITS = '23456789abcdefghjkmnpqrstuvwxyz'

# Offset the referral code with this amount. This is to prevent single-digit
# or double-digit codes, if you care about that kind of thing.
PRELAUNCH_OFFSET = 1200

# The referral code typically looks something like this by default:
# http://yourdomain.com/?referrer=3hg6sl
# You can change the parameter name to something that does not clash with other
# apps or looks nicer.
PRELAUNCH_PARAMETER_NAME = 'referrer'

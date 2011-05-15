While developing the next Facebook, you want to get some buzz going, get beta-testers and start building your list of interested people. This app lets you do that.

Prelaunch provides you with a couple of tools to put up a simple buzz-generating and information-gathering pre-launch page.

Current functionality:
----------------------

* A simple signup form asking for email.
* A referral code for each signup, used to refer other people to the site.
* Tracking of the referral code, so that you can identify prolific referrers.
* An example of how to show a QR code image of the referral code, for easy distribution.

Future planned functionality:
---------------------

* Admin functionality to convert prelaunch emails to user accounts.
* Hooks to automatically create user accounts after a specified number of referrals.
* Analytics integration to track where the referrers come from.
* Counting referrals that do not sign up.
* Getting the domain from the sites framework and populating the welcome message using the domain.

Some design considerations:
---------------------------

We do not create user accounts immediately, since that reduces flexibility. Forcing the creation of user accounts bloats the user account system.

The referral code should be as short as possible. We use a list of allowed characters. The code looks like a shorturl code. We remove easily-confused characters like 1 and l, 0 and O, etc. to make it easy to read and give out to other people.

How to get started:
-------------------

In your settings.py:

    * Make sure you include 'django.core.context_processors.request' in your context processors.

    * Add 'prelaunch' to your installed apps.

    * Include Override some of the settings in the app settings.py file with your own in your project settings.py, if needed.

Now you can add a prelaunch form in a template by doing the following:

    * add a {% load prelaunch_tags %} template tag to the template
    * Add a {% prelaunch_form %} tag where you want the form to appear.
    * Customise the templates to your liking by copying them into the templates/prelaunch directory in your project and changing them.

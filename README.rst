While developing the next Facebook, you want to get some buzz going, get beta-testers and start building your list of interested people. This app lets you do that.

Prelaunch provides you with a couple of tools to put up a simple buzz-generating and information-gathering setup.

Current functionality:
----------------------

* A simple signup form asking for email.
* A referral code for each signup, used to refer other people to the site.
* QR code image of the referral code, for easy distribution.
* Tracking of the referral code, so that you see prolific referrers.

Future functionality:
---------------------

* Admin functionality to convert prelaunch emails to user accounts.
* Hooks to automatically create user accounts after a specified number of referrals.
* Analytics integration to track where the referrers come from.
* Counting referrals that do not sign up.

Some design considerations:
---------------------------

We do not create user accounts immediately, since that reduces flexibility. Forcing the creation of user accounts bloats the user account system. However, if a user account is created, the prelaunch info is surfaced as a profile.

The referral code should be as short as possible. We use a list of allowed characters. The code looks like a shorturl code. We remove easily-confused characters like 1 and l, 0 and O, etc. to make it easy to read and give out to other people.

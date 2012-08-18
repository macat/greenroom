greenroom
=========

GREENROOM

##-- to run locally --#

1) create /tmp/outfits to store uploaded outfits' pictures
2) create settings_local.py and put there: 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
HOST = 'http://localhost:8000'
3) run syncdb (no admin user)

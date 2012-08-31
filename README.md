greenroom
=========

GREENROOM

1) DEV MODE: to run project without collecting static files

./manage runserver


2) TEST MODE: to run the project with collected static files:

./runserver-greenroom.sh


3) sample settings_local.py

##-- helpers --##
import os

# expects a list
prepend_path_with_root = lambda *l: os.path.join(os.getcwd(), *l)


##-- settings --##

HOST = 'http://localhost.mygreenroom.herokuapp.com:8000'

DEBUG = TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': prepend_path_with_root('greenroom.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# not sending files to Amazon
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
MEDIA_ROOT = '/tmp/media'
MEDIA_URL = '/media/'

# development static files handling
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_DIRS = (prepend_path_with_root('static'),
                    prepend_path_with_root('greenroom', 'apps', 'django_facebook_patched', 'static'))
STATIC_ROOT = '/tmp/static'
STATIC_URL = '/static/'

## not compressing and combining files
PIPELINE = False

# not sending emails via mailgun
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# enabling Facebook authorization and login
# also add an alias in /etc/hosts: mygreenroom.herokuapp.com http://localhost.mygreenroom.herokuapp.com:8000
FACEBOOK_APP_ID = 'ask-someone'
FACEBOOK_APP_SECRET = 'ask-someone'
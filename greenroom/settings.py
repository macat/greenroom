##-- helpers --##
import os

# expects a list
prepend_path_with_root = lambda *l: os.path.join(os.getcwd(), *l)


##-- settings --##

DEBUG = TEMPLATE_DEBUG = False

ADMINS = MANAGERS = (
    ('virtuallight', 'mat.jankowski@gmail.com'),
    ('macat', 'attila@maczak.hu')
)

# Heroku db settings
import dj_database_url
DATABASES = {'default': dj_database_url.config()}

TIME_ZONE = 'UTC'
USE_TZ = True
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATICFILES_DIRS = (prepend_path_with_root('static'),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SITE_ID = 1
SECRET_KEY = '34lef7ul)&amp;-b6d_-ug(8t^n0($))g$05grb%alr5l+mrjcla3!'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'greenroom.apps.django_facebook_patched.context_processors.facebook',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
    prepend_path_with_root('greenroom','templates'),
)

ROOT_URLCONF = 'greenroom.urls'
WSGI_APPLICATION = 'greenroom.wsgi.application'

INSTALLED_APPS = (
    'pipeline',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'greenroom.apps.feedback',
    'greenroom.apps.outfit',
    'greenroom.apps.www',
    'greenroom.apps.django_facebook_patched',
)

AUTH_PROFILE_MODULE = 'django_facebook_patched.FacebookProfile'
AUTHENTICATION_BACKENDS = (
    'greenroom.apps.django_facebook_patched.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


##-- custom settings --##

HOST = 'http://mygreenroom.herokuapp.com'

# Amazon S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', '')

STATICFILES_STORAGE = 'greenroom.libs.staticfile_storage.S3PipelineStorage'
STATIC_URL = '/https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME

# combined, compressed and versioned static files
PIPELINE = True
PIPELINE_AUTO = False
PIPELINE_VERSION = True
PIPELINE_JS = {
    'scripts-basic-libs': {
        'source_filenames': (
          'scripts/basic-libs/*.js',
        ),
        'output_filename': 'pipeline_scripts-basic-libs.js',
    },
    'scripts-libs': {
        'source_filenames': (
          'scripts/libs/*.js',
        ),
        'output_filename': 'pipeline_scripts-libs.js',
    },
    'scripts': {
        'source_filenames': (
          'scripts/*.js',
          'js/*.js'
        ),
        'output_filename': 'pipeline_scripts.js',
    },
}

PIPELINE_CSS = {
    'styles': {
        'source_filenames': (
          'styles/stylesheets/style.css',
          'css/*.css',
        ),
        'output_filename': 'pipeline_styles.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    }
}

# Facebook
FACEBOOK_APP_ID = os.getenv('FACEBOOK_APP_ID', '')
FACEBOOK_APP_SECRET = os.getenv('FACEBOOK_APP_SECRET', '')

## Mailgun 
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = os.getenv('MAILGUN_ACCESS_KEY', '')
MAILGUN_SERVER_NAME = os.getenv('MAILGUN_SERVER_NAME', '')

try:
    from settings_local import *
except ImportError:
    pass

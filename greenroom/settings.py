##-- helpers --##
import os

# expects a list
prepend_path_with_root = lambda *l: os.path.join(os.getcwd(), *l)


##-- settings --##

# Django settings for greenroom project.

DEBUG = TEMPLATE_DEBUG = True

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
STATIC_URL = '/static/'
STATICFILES_DIRS = ()
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
    'django_facebook.context_processors.facebook',
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
    'greenroom.apps.outfit',
    'greenroom.apps.www',
    'django_facebook',
)

AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'
AUTHENTICATION_BACKENDS = (
    'django_facebook.auth_backends.FacebookBackend',
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

# custom settings 

HOST = 'http://greenroom-app.herokuapp.com'
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE = not DEBUG

PIPELINE_JS = {
    'scripts': {
        'source_filenames': (
          'scripts/libs/*.js',
          'scripts/*.js',
        ),
        'output_filename': 'scripts.js',
    }
}

# Facebook integration
FACEBOOK_APP_ID = '104170716399805'
FACEBOOK_APP_SECRET = '95b73050a1b74289b84c12a900620162'

try:
    from settings_local import *
except ImportError:
    pass

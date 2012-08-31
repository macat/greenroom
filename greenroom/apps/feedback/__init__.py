from django.conf import settings

if not hasattr(settings, 'DEFAULT_FEEDBACK_FROM_EMAIL'):
    settings.DEFAULT_FEEDBACK_FROM_EMAIL = "friend@greenroomapp.com"
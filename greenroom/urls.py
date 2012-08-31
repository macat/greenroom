from django.conf import settings
from django.conf.urls import include, patterns, url

import greenroom.apps.feedback.views as feedback_views
import greenroom.apps.outfit.views as outfit_views
import greenroom.apps.www.views as www_views


urlpatterns = patterns('',
    # apps.www
    url(r'^$', www_views.home, name='www_home'),
    # apps.outfit
    url(r'^outfit/new$', outfit_views.new_outfit, name='outfit_new_outfit'),
    url(r'^outfit/list$', outfit_views.list_outfits, name='outfit_list_outfits'),
    url(r'^outfit/(?P<uuid>.{6})$', outfit_views.view_outfit, name='outfit_view_outfit'),
    url(r'^outfit/(?P<uuid>.{6})/request_feedback$', outfit_views.request_feedback, name='outfit_request_feedback'),
    url(r'^outfit/feedback/(?P<uuid>.{6})$', feedback_views.give_feedback, name='outfit_give_feedback'),
    # django-facebook
    (r'^facebook/', include('greenroom.apps.django_facebook_patched.urls')),
    (r'^accounts/', include('greenroom.apps.django_facebook_patched.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
)


# only enabled when runserver started with --nostatic, then remember to collectstatic first
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

from django.conf.urls import include, patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import greenroom.apps.outfit.views as outfit_views
import greenroom.apps.www.views as www_views


urlpatterns = patterns('',
    # apps.www
    url(r'^$', www_views.home, name='www_home'),
    # apps.outfit
    url(r'^outfit/new$', outfit_views.new_outfit, name='outfit_new_outfit'),
    url(r'^outfit/(?P<uuid>.{6})$', outfit_views.view_outfit, name='outfit_view_outfit'),
    url(r'^outfit/(?P<uuid>.{6})/request_feedback$', outfit_views.request_feedback, name='outfit_request_feedback'),
    url(r'^outfit/feedback/(?P<uuid>.{6})$', outfit_views.give_feedback, name='outfit_give_feedback'),
    # django-facebook
    (r'^facebook/', include('django_facebook.urls')),
    (r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
)

urlpatterns += staticfiles_urlpatterns()

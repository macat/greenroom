from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import greenroom.apps.outfit.views as outfit_views
import greenroom.apps.www.views as www_views


urlpatterns = patterns('',
    url(r'^$', www_views.HomeView.as_view(), name='www_home'),
    url(r'^outfit/new$', outfit_views.new_outfit, name='outfit_new_outfit'),
    url(r'^outfit/(?P<uuid>.{6})$', outfit_views.view_outfit, name='outfit_view_outfit'),
    url(r'^outfit/(?P<uuid>.{6})/request_feedback$', outfit_views.request_feedback, name='outfit_request_feedback'),
    url(r'^outfit/feedback/(?P<uuid>.{6})$', outfit_views.give_feedback, name='outfit_give_feedback'),
)

urlpatterns += staticfiles_urlpatterns()

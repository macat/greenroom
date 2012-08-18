from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import greenroom.apps.outfit.views as outfit_views
import greenroom.apps.www.views as www_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', www_views.HomeView.as_view(), name='www_home'),
    url(r'^outfit/new$', outfit_views.NewView.as_view(), name='outfit_new'),
    url(r'^outfit/submit?$', outfit_views.SubmitView.as_view(), name='outfit_submit'),
    url(r'^outfit/view/(?P<uuid>.{6})$', outfit_views.ViewView.as_view(), name='outfit_view'),
    url(r'^outfit/feedback/(?P<uuid>.{6})$', outfit_views.FeedbackView.as_view(), name='outfit_feedback'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

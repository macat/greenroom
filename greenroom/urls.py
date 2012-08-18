from django.conf.urls import patterns, include, url

from greenroom.apps.outfit.views import OutfitNewView
from greenroom.apps.www.views import WWWHomeView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', WWWHomeView.as_view(), name='www_home'),
    url(r'^outfit/new$', OutfitNewView.as_view(), name='outfit_new'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

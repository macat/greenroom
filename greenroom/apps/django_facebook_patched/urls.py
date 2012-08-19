from django.conf.urls.defaults import patterns, url
from greenroom.apps.django_facebook_patched import settings as facebook_settings

urlpatterns = patterns('greenroom.apps.django_facebook_patched.views',
   url(r'^connect/$', 'connect', name='facebook_connect'),
   url(r'^image_upload/$', 'image_upload', name='facebook_image_upload'),
   url(r'^wall_post/$', 'wall_post', name='facebook_wall_post'),
   url(r'^canvas/$', 'canvas', name='facebook_canvas'),
)




#help autodiscovery a bit
from greenroom.apps.django_facebook_patched import admin

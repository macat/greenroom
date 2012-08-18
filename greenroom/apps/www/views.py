from django.shortcuts import render_to_response
from django.template import RequestContext

from .helpers import get_facebook_friends
        

def home(request):
    # user might be authenticated and logged in only via Facebook (no other auth possibility)
    fb_friends = get_facebook_friends(request) if request.user.is_authenticated() else []
    return render_to_response('home.html',
                              {'fb_friends': fb_friends},
                              context_instance=RequestContext(request))

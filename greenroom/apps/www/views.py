from django.shortcuts import render
from django.template import RequestContext

from .helpers import get_facebook_friends
        

def home(request):
    # user might be authenticated and logged in only via Facebook (no other auth possibility)
    fb_friends = get_facebook_friends(request) if request.user.is_authenticated() else []
    return render('home.html', {'fb_friends': fb_friends})

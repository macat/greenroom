from django.shortcuts import render

#from .helpers import get_facebook_friends
        

def home(request):
#    # user might be authenticated and logged in only via Facebook (no other auth possibility)
#    fb_friends = get_facebook_friends(request) if request.user.is_authenticated() else []
    return render(request, 'home.html')#, {'fb_friends': fb_friends})

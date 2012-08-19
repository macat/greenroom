import binascii
import re
from datetime import datetime

from greenroom.apps.django_facebook_patched.api import FacebookUserConverter, get_persistent_graph
from open_facebook.api import FacebookAuthorization
    
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils import simplejson

from .models import Outfit, OutfitFeedback


def get_and_create_outfit_from_reqeust(request):
    outfit = Outfit.objects.create()
    # file from uploader or webcam
    cf_content = request.read(10485760) if 'qqfile' in request.GET else binascii.unhexlify(request.raw_post_data)
    outfit.img.save('%s.jpg' % outfit.uuid, ContentFile(cf_content))
    return outfit
    
def add_description_to_outfit(outfit, description):
    outfit.description = description
    outfit.save()

def create_and_send_feedback_requests(request, outfit):
    sender = get_users_fb_email(request) if request.user.is_authenticated else "friend@greenroomapp.com" 
    recipients_list = [v for k,v in request.POST.items() if k.startswith('email_') and v]
    for recipient in recipients_list:
        outfit_feedback = OutfitFeedback.objects.create(outfit=outfit, emailed_to=recipient)
        send_mail('I urgently need your advice!',
                  'Please give me feedback: ' + outfit_feedback.feedback_url, 
                  sender, 
                  [recipient],
                  fail_silently=False)

def give_outfit_feedback(rating, comment, outfit_feedback):
    outfit_feedback.rating = rating
    outfit_feedback.comment = comment
    outfit_feedback.answered_at = datetime.now()
    outfit_feedback.save()
    
def bind_user_with_outfit(user, outfit):
    if user.is_authenticated() and not outfit.user:
        outfit.user = user
        outfit.save()

def get_users_fb_email(request):
    app_access_token = FacebookAuthorization.get_cached_app_access_token()
    graph = get_persistent_graph(request, access_token=app_access_token)
    return graph.me()['email']
        
class JSONResponse(HttpResponse):
    def __init__(self, request, data):
        indent = 2 if settings.DEBUG else None
        mime = "text/javascript" if settings.DEBUG else "application/json"
        content = simplejson.dumps(data, indent=indent)
        callback = request.GET.get('callback')
        if callback:
            # verify that the callback is only letters, numbers, periods, and underscores
            if re.compile(r'^[a-zA-Z][\w.]*$').match(callback):
                content = '%s(%s);' % (callback, content)
        super(JSONResponse, self).__init__(
            content = content,
            mimetype = mime,
        )
    

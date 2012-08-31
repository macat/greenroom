import re
from StringIO import StringIO

from greenroom.apps.django_facebook_patched.api import get_persistent_graph
from open_facebook.api import FacebookAuthorization
    
from django.conf import settings
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.utils import simplejson

from greenroom.apps.feedback import api as feedback_api 

from .models import Outfit


def get_and_create_outfit_from_reqeust(request):
    outfit = Outfit.objects.create()
    # file from uploader or webcam
    if 'qqfile' in request.GET:
        cf_content = request.read(10485760)
        outfit.img.save('%s.jpg' % outfit.uuid, ContentFile(cf_content))
    else:
        raw_data = request.POST['image'][len('data:image/png;base64,'):].decode('base64')
        buf = StringIO(raw_data)
        buf.seek(0, 2)
        filename = '%s.jpg' % outfit.uuid
        f = ContentFile(buf.getvalue())
        outfit.img.save(filename, f)
    return outfit
    
def add_description_to_outfit(outfit, description):
    outfit.description = description
    outfit.save()

def create_and_send_feedback_requests(request, outfit):
    # facebook
    fb_emails = [v for k,v in request.POST.items() if k.startswith('email_fb_') and v]
    fb_sender = get_users_fb_email(request) if request.user.is_authenticated() else "friend@greenroomapp.com" 
    feedback_api.send_mass_facebook_request(outfit.pk, fb_emails, fb_sender)
    
    # email
    emails = [v for k,v in request.POST.items() if k.startswith('email_') and \
              not k.startswith('email_fb_') and v]
    sender = fb_sender
    feedback_api.send_mass_email_request(outfit.pk, emails, sender)

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
    

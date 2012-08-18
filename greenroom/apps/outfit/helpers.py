import re

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils import simplejson

from .models import OutfitFeedback


def create_and_send_feedback_requests(outfit, recipients_list):
    for rec in recipients_list:
        outfit_feedback = OutfitFeedback.objects.create(outfit=outfit, emailed_to=rec)
        send_mail('I urgently need your advice!',
                  'Please give me feedback: ' + outfit_feedback.feedback_url, 
                  'friend@greenroom.com', 
                  [rec],
                  fail_silently=False)
        
def give_outfit_feedback(outfit_feedback, rating):
    outfit_feedback.rating = rating
    outfit_feedback.is_used = True
    outfit_feedback.save()
    
    
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
    
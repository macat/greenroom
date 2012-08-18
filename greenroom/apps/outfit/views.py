import base64
import binascii
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from .forms import OutfitForm
from .helpers import create_and_send_feedback_requests, give_outfit_feedback, JSONResponse
from .models import Outfit, OutfitFeedback

@csrf_exempt
def new_outfit(request):
    if request.method == 'POST':

        with open('file.jpg', 'w+') as f:
            f.write(binascii.unhexlify(request.raw_post_data))
        form = OutfitForm(request.POST, request.FILES)
        if form.is_valid():
            outfit = form.save()
            outfit.save()
            # success - new outfit uploaded
            return JSONResponse(request,
                                {'request_feedback_url': reverse('outfit_request_feedback', args=[outfit.uuid])})
    # failure
    return JSONResponse(request, {})
 
def view_outfit(request, uuid):
    return render('view.html', {'outfit': Outfit.objects.get(uuid=uuid)})

def request_feedback(request, uuid):        
    if request.method == 'POST':
        outfit = Outfit.objects.get(uuid=uuid)
        recipients_list = [v for k,v in request.POST.items() if k.startswith('email_') and v]
        create_and_send_feedback_requests(outfit, recipients_list)
        # success - feedback request sent out
        return redirect(outfit.view_url)
    # failure
    return HttpResponseNotAllowed()
    
def give_feedback(request, uuid):
    outfit_feedback = OutfitFeedback.objects.get(uuid=uuid)
    
    if outfit_feedback.is_used:
        # failure - feedback already given
        return redirect(outfit_feedback.outfit.view_url)
    
    if request.method == 'POST':
        give_outfit_feedback(outfit_feedback, request.POST['rating'])
        # success
        return redirect(outfit_feedback.outfit.view_url)
    
    return render('feedback.html', {'outfit_feedback': outfit_feedback})

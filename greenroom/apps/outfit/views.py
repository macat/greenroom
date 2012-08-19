from django.core.urlresolvers import reverse
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .helpers import (create_and_send_feedback_requests,
                      give_outfit_feedback,
                      JSONResponse,
                      get_and_create_outfit_from_reqeust,
                      bind_user_with_outfit)
from .models import Outfit, OutfitFeedback


@csrf_exempt
def new_outfit(request):
    if request.method == 'POST':
        outfit = get_and_create_outfit_from_reqeust(request)
        if outfit:
            # success
            return JSONResponse(request,
                    {'success': True,
                     'request_feedback_url': reverse('outfit_request_feedback', args=[outfit.uuid])})
    # failure
    return JSONResponse(request, {})
 
def list_outfits(request):
    return render(request, 'list.html',
                  {'outfits': request.user.outfit_set.all() if request.user.is_authenticated() else []})

def view_outfit(request, uuid):
    return render(request, 'view.html', {'outfit': Outfit.objects.get(uuid=uuid)})

def request_feedback(request, uuid):        
    if request.method == 'POST':
        outfit = Outfit.objects.get(uuid=uuid)
        recipients_list = [v for k,v in request.POST.items() if k.startswith('email_') and v]
        create_and_send_feedback_requests(outfit, recipients_list)
        bind_user_with_outfit(request.user, outfit)
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
    
    return render(request, 'feedback.html', {'outfit_feedback': outfit_feedback})

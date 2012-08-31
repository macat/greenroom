from django.core.urlresolvers import reverse
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from greenroom.apps.feedback import api as feedback_api 

from .helpers import (create_and_send_feedback_requests,
                      JSONResponse,
                      get_and_create_outfit_from_reqeust,
                      bind_user_with_outfit,
                      add_description_to_outfit)
from .models import Outfit


@csrf_exempt
def new_outfit(request):
    if request.method == 'POST':
        outfit = get_and_create_outfit_from_reqeust(request)
        if outfit:
            # success
            return JSONResponse(request,
                    {'success': True,
                     'request_feedback_url': reverse('outfit_request_feedback', args=[outfit.uuid]),
                     'img': outfit.img.url})
    # failure
    return JSONResponse(request, {})
 
def list_outfits(request):
    return render(request, 'list.html',
                  {'outfits': request.user.outfit_set.all().order_by('-submitted_at') if request.user.is_authenticated() else []})

def view_outfit(request, uuid):
    outfit = Outfit.objects.get(uuid=uuid)
    outfitfeedback_list = feedback_api.get_outfitfeedback_list(outfit.pk)
    return render(request, 'view.html', {'outfit': outfit,
                                         'outfitfeedback_list': outfitfeedback_list})

def request_feedback(request, uuid):        
    if request.method == 'POST':
        outfit = Outfit.objects.get(uuid=uuid)
        add_description_to_outfit(outfit, request.POST['description'])
        create_and_send_feedback_requests(request, outfit)
        bind_user_with_outfit(request.user, outfit)
        # success - feedback request sent out
        return redirect(outfit.view_url)
    
    # failure
    return HttpResponseNotAllowed('')
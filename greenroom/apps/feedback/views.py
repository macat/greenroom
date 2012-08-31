from django.shortcuts import redirect, render

from .helpers import give_outfit_feedback
from .models import OutfitFeedback


def give_feedback(request, uuid):
    outfit_feedback = OutfitFeedback.objects.get(uuid=uuid)
    
    if outfit_feedback.answered_at:
        # failure - feedback already given
        return redirect(outfit_feedback.outfit.view_url)
    
    if request.method == 'POST' and request.POST.get('rating'):
        give_outfit_feedback(request.POST['rating'], request.POST['comment'], outfit_feedback)
        # success
        return redirect(outfit_feedback.outfit.view_url)
    
    return render(request, 'feedback.html', {'outfit_feedback': outfit_feedback})
from django.shortcuts import redirect
from django.views.generic import TemplateView

from .models import Outfit, OutfitFeedback
from .helpers import create_and_send_feedback_requests, give_outfit_feedback


class NewView(TemplateView):
    template_name = "new.html"
    
    def post(self, *args, **kwargs):
        return self.get(*args, **kwargs)
    
class SubmitView(TemplateView):
    def post(self, request, *args, **kwargs):
        outfit = Outfit.objects.create()
        recipients_list = [v for k,v in request.POST.items() if k.startswith('email_') and v]
        create_and_send_feedback_requests(outfit, recipients_list)
        return redirect(outfit.view_url)
    
class ViewView(TemplateView):
    template_name = "view.html"
    
    def get_context_data(self, **kwargs):
        context = super(ViewView, self).get_context_data(**kwargs)
        context['outfit'] = Outfit.objects.get(uuid=kwargs['uuid'])
        return context
    
class FeedbackView(TemplateView):
    template_name = "feedback.html"
    
    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['outfit_feedback'] = OutfitFeedback.objects.get(uuid=kwargs['uuid'])
        return context
    
    def get(self, *args, **kwargs):
        outfit_feedback = OutfitFeedback.objects.get(uuid=kwargs['uuid'])
        if not outfit_feedback.is_used:
            return super(FeedbackView, self).get(*args, **kwargs)
        else:
            return redirect(outfit_feedback.outfit.view_url)
            
    def post(self, request, *args, **kwargs):
        outfit_feedback = OutfitFeedback.objects.get(uuid=kwargs['uuid'])
        if not outfit_feedback.is_used:
            give_outfit_feedback(outfit_feedback, request.POST['rating'])
        return redirect(outfit_feedback.outfit.view_url)
        

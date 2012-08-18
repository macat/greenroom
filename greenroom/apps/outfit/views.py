from django.shortcuts import redirect
from django.views.generic import TemplateView, RedirectView


class NewView(TemplateView):
    template_name = "new.html"
    
    def post(self, *args, **kwargs):
        return self.get(*args, **kwargs)
    
class SubmitView(RedirectView):
    url = '/outfit/view'
    
class ViewView(TemplateView):
    template_name = "view.html"
    
class FeedbackView(TemplateView):
    template_name = "feedback.html"
    
    def post(self, *args, **kwargs):
        return redirect('/outfit/view')
        

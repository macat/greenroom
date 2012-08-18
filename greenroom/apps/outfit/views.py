from django.shortcuts import redirect
from django.views.generic import TemplateView, RedirectView


class NewView(TemplateView):
    template_name = "new.html"
    
    def post(self, *args, **kwargs):
        return self.get(*args, **kwargs)
    
class SubmitView(RedirectView):
    url = '/outfit/view/' + 'abc123' # + fake uuid
    
class ViewView(TemplateView):
    template_name = "view.html"
    
class FeedbackView(TemplateView):
    template_name = "feedback.html"
    
    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['outfit'] = {'uuid': 'abc123'} # fake outfit + fake uuid
        return context
    
    def post(self, *args, **kwargs):
        return redirect('/outfit/view/' + 'abc123') # + fake uuid
        

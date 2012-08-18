from django.views.generic import TemplateView


class WWWHomeView(TemplateView):
    template_name = "home.html"

from django.views.generic import TemplateView


class OutfitNewView(TemplateView):
    template_name = "new.html"
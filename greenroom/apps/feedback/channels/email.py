from django.core.mail import send_mail

from ..models import OutfitFeedback


def send_request(outfit_pk, recipient, sender):
    outfit_feedback = OutfitFeedback.objects.create(outfit_pk=outfit_pk, emailed_to=recipient)
    send_mail('I urgently need your advice!',
              'Please give me feedback: ' + outfit_feedback.feedback_url, 
              sender, 
              [recipient],
              fail_silently=False)
from django.core.mail import send_mail

from .models import OutfitFeedback


def create_and_send_feedback_requests(outfit, recipients_list):
    for rec in recipients_list:
        outfit_feedback = OutfitFeedback.objects.create(outfit=outfit, emailed_to=rec)
        send_mail('I urgently need your advice!',
                  'Please give me feedback: ' + outfit_feedback.feedback_url, 
                  'friend@greenroom.com', 
                  [rec],
                  fail_silently=False)
        
def give_outfit_feedback(outfit_feedback, rating):
    outfit_feedback.rating = rating
    outfit_feedback.is_used = True
    outfit_feedback.save()
    
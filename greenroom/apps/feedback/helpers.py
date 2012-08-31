from datetime import datetime


def retrieve_outfit(outfit_pk):
    from greenroom.apps.outfit.models import Outfit
    return Outfit.objects.get(pk=outfit_pk)

def give_outfit_feedback(rating, comment, outfit_feedback):
    outfit_feedback.rating = rating
    outfit_feedback.comment = comment
    outfit_feedback.answered_at = datetime.now()
    outfit_feedback.save()
    

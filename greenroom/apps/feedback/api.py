from .channels import facebook as facebook_channel
from .channels import email as email_channel
from .helpers import retrieve_outfit
from .models import OutfitFeedback


def get_avarage_rating(outfit_pk):
        outfit = retrieve_outfit(outfit_pk)
        ratings = outfit.outfitfeedback_set.filter(answered_at__isnull=False).values_list('rating', flat=True)
        if ratings:
            return float(sum(ratings))/float(len(ratings))
        else:
            return 0.0

def get_outfitfeedback_list(outfit_pk):
    return list(OutfitFeedback.objects.filter(outfit_pk=outfit_pk))
        
def send_mass_facebook_request(outfit_pk, emails, sender):
    for email in emails:
        facebook_channel.send_request(outfit_pk, email, sender)

def send_mass_email_request(outfit_pk, emails, sender):
    for email in emails:
        email_channel.send_request(outfit_pk, email, sender)

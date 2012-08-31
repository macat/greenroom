import random
import string

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from .helpers import retrieve_outfit


def generate_uuid():
    # return a 6-char string random of letters and digits e.g. 4Gcr92
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))
    
class OutfitFeedback(models.Model):
    RATING_CHOICES = ((1,1), (2,2), (3,3), (4,4), (5,5))

    uuid = models.CharField(max_length=6, default=generate_uuid, editable=False, primary_key=True) # auto-generated
    outfit_pk = models.CharField(max_length=6) # fits the uuid of the outfit
    rating = models.IntegerField(max_length=1, choices=RATING_CHOICES, null=True, blank=True)
    requested_at = models.DateTimeField(auto_now_add=True, editable=False)
    answered_at = models.DateTimeField(editable=False, null=True, blank=True)

    emailed_to = models.EmailField()
    comment = models.TextField()

    @property
    def outfit(self):
        return retrieve_outfit(self.outfit_pk)

    @property
    def rating_doubled(self):
        return self.rating * 2
        
    @property
    def feedback_url(self):
        """Sharable URL for outfit feedback giving"""
        return settings.HOST + self.get_absolute_url()

    def get_absolute_url(self):
        return reverse('outfit_give_feedback', args=[self.uuid])
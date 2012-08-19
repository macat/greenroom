import random
import string

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


def generate_uuid():
    # return a 6-char string random of letters and digits e.g. 4Gcr92
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))

class Outfit(models.Model):
    uuid = models.CharField(max_length=6, default=generate_uuid, editable=False, primary_key=True) # auto-generated
    img = models.ImageField(upload_to='outfits')
    user = models.ForeignKey(User, editable=False, null=True, blank=True)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True, editable=False)

    def get_absolute_url(self):
        return reverse('outfit_view_outfit', args=[self.uuid])
    
    @property
    def avg_rating(self):
        """Avarage from all ratings"""
        ratings = self.outfitfeedback_set.filter(answered_at__isnull=False).values_list('rating', flat=True)
        if ratings:
            return float(sum(ratings))/float(len(ratings))
        else:
            return 0.0
    
    @property
    def view_url(self):
        """Sharable URL for outfit feedback viewing"""
        return settings.HOST + self.get_absolute_url()
    
    
class OutfitFeedback(models.Model):
    RATING_CHOICES = ((1,1), (2,2), (3,3), (4,4), (5,5))

    uuid = models.CharField(max_length=6, default=generate_uuid, editable=False, primary_key=True) # auto-generated
    outfit = models.ForeignKey(Outfit)
    emailed_to = models.EmailField()
    rating = models.IntegerField(max_length=1, choices=RATING_CHOICES, null=True, blank=True)
    comment = models.TextField()
    requested_at = models.DateTimeField(auto_now_add=True, editable=False)
    answered_at = models.DateTimeField(editable=False, null=True, blank=True)

    def rating_doubled(self):
        return self.rating * 2

    def get_absolute_url(self):
        return reverse('outfit_give_feedback', args=[self.uuid])
        
    @property
    def feedback_url(self):
        """Sharable URL for outfit feedback giving"""
        return settings.HOST + self.get_absolute_url()

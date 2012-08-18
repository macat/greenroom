import random
import string

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


def generate_uuid():
    # return a 6-char string random of letters and digits e.g. 4Gcr92
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))

class Outfit(models.Model):
    uuid = models.CharField(max_length=6, default=generate_uuid, editable=False, primary_key=True) # auto-generated
    img = models.ImageField(upload_to='/tmp/outfits')

    def get_absolute_url(self):
        return reverse('outfit_view', args=[self.uuid])
    
    @property
    def avg_rating(self):
        """Avarage from all ratings"""
        raise NotImplementedError()
    
    @property
    def view_url(self):
        """Sharable URL for outfit feedback viewing"""
        return settings.HOST + self.get_absolute_url()
    
class OutfitFeedback(models.Model):
    RATING_CHOICES = ((1,1), (2,2), (3,3), (4,4), (5,5))

    uuid = models.CharField(max_length=6, default=generate_uuid, editable=False, primary_key=True) # auto-generated
    outfit = models.ForeignKey(Outfit)
    emailed_to = models.EmailField()
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    is_used = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('outfit_feedback', args=[self.uuid])
        
    @property
    def feedback_url(self):
        """Sharable URL for outfit feedback giving"""
        return settings.HOST + self.get_absolute_url()
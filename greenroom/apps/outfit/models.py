import random
import string

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from greenroom.apps.feedback import api as feedback_api


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
        return feedback_api.get_avarage_rating(self.id)
    
    @property
    def view_url(self):
        """Sharable URL for outfit feedback viewing"""
        return settings.HOST + self.get_absolute_url()
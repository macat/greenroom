from django.db import models


class Outfit(models.Model):
#    img =
    
    @property
    def avg_rating(self):
        """Avarage from all ratings."""
        raise NotImplementedError()
    
class OutfitFeedback(models.Model):
#    outfit = 
#    uuid = 
##
#    rating = 

    @property
    def url(self):
        """Sharable URL for outfit rating.""" 
        raise NotImplementedError()
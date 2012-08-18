from django.db import models


class Outfit(models.Model):
#    img =
#    title =
    
    @property
    def avg_rating(self):
        """Avarage from all ratings."""
        raise NotImplementedError()
    
class OutfitFeedback(models.Model):
#    outfit = 
#    uuid = 
##
#    rating = 
#    comment = 

    @property
    def url(self):
        """Sharable URL for outfit rating.""" 
        raise NotImplementedError()
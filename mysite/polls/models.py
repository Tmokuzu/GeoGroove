from django.db import models

# Create your models here.

class Music(models.Model):
    MusicTitle = models.CharField(max_length=255)
    ArtistName = models.CharField(max_length=255)
    Country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.MusicTitle
    
    #def update_DB(self, MusicDB):
        
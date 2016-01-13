from django.db import models

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length = 20)
    artist = models.CharField(max_length = 30)
    catgry = models.CharField(max_length = 10)
    date = models.DateField()
    
    def __unicode__(self):
        return self.title
    
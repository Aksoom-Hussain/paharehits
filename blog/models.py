from django.db import models

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length = 20,null=False, blank =False )
    artist = models.CharField(max_length = 30,blank=True , default = "unknown")
    catgry = models.CharField(max_length = 10,null=False, blank =False )
    dwn =models.CharField(max_length = 200,null=False, blank =False )
    date = models.DateTimeField()
    
    
    def __unicode__(self):
        return self.title
    
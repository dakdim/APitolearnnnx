from django.db import models

# Create your models here.

class Moviedata(models.Model):
    
    def __str__ (self):
           return self.name
        #    return super().__str__()
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()

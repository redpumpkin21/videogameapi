from django.db import models

    
# Create your models here.
class Videogames(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)    
    genre = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=1000000)
    video =  models.CharField(max_length=1000)
    image = models.CharField(max_length=100000)
    trailer =  models.CharField(max_length=1000)
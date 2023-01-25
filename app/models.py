from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Visit(models.Model):
    count = models.IntegerField(default=0)
    
class Video(models.Model):
    link = models.TextField()
from django.db import models

class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    taker = models.CharField(max_length=128)
    message = models.TextField(max_length=1024)
    latitude = models.FloatField()
    longitude = models.FloatField()

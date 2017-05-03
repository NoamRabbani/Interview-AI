from django.db import models

# Create your models here.

class Match(models.Model):
    match_name = models.CharField(max_length=200)
    match_date = models.DateTimeField('date published')

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    limitdate = models.DateField('limitdate')
    adminonly = models.BooleanField()
from django.db import models
from django.conf import settings
from django.utils import timezone

class Article(models.Model):
    adminonly = models.BooleanField()
    body = models.CharField(max_length=2000)
    description = models.CharField(max_length=200)
    limitdate = models.DateField('limitdate')
    created_date = models.DateTimeField(default=timezone.now)
    release = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.release = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Meta:
    ordering = ['title', 'limitedate']
    release = models.DateField('limitdate')    
    title = models.CharField(max_length=60)
    

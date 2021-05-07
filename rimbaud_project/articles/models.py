from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    limitdate = models.DateField('limitdate')
    adminonly = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    release = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.release = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Meta:
    ordering = ['title', 'limitedate']

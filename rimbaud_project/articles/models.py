from django.db import models
from django.conf import settings
from django.utils import timezone

class Article(models.Model):
    adminonly = models.BooleanField('Admin only')
    body = models.TextField('Corps de l\'article', max_length=2000)
    description = models.CharField('Description', max_length=200)
    limitdate = models.DateTimeField('Date de péremption')
    title = models.CharField('Titre de l\'article', max_length=60)
    release = models.DateTimeField('Date de publication', default=timezone.now())

    def publish(self):
        self.release = timezone.now()
        self.save()

#     def __str__(self):
#         return self.title

# class Meta:
#     ordering = ['title', 'limitedate']
#     release = models.DateField('limitdate')    
#     title = models.CharField(max_length=60)
    

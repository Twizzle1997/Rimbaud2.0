from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.conf import include
from articles.models import Article
from django.http import HttpResponse
import datetime

def index(request):
    articles = Article.objects.filter(limitdate__range=[datetime.datetime.now(), '3021-12-31']).order_by('release')
    return render(request, template_name='articles_list.html', context={'articles':articles})

def article(request, id):
    HttpResponse('Hello')
    article = Article.objects.get(id=id)
    return render(request, template_name='article_view.html', context={'article':article})
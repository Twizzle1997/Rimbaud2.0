from django.shortcuts import render
from django.urls.conf import include
from articles.models import Article

def index(request):
    articles = Article.objects.all().order_by('release')
    return render(request, template_name='articles_list.html', context={'articles':articles})

def article(request, id):
    article = Article.objects.get(id=id)
    return render(request, template_name='article_view.html', context={'article':article})
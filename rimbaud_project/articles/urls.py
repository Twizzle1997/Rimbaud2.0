from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='all_articles'),
    path('article', views.article, name='article_view'),
]

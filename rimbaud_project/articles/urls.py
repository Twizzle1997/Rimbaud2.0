from django.urls import path, include
from . import views

urlpatterns = [
    path('article/<int:id>/', views.article, name='article_view'),
    path('', views.index, name='all_articles'),    
]

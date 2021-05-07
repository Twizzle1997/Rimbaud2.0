from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='all_articles'),
    path('article/<int:id>/', views.article, name='article_view'),
    path('search/<str:words>', views.search, name='article_search')
]

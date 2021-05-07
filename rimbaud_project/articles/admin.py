from django.contrib import admin
from .models import Article


@admin.register(Article)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'body', 'limitdate', 'adminonly', 'created_date', 'release')

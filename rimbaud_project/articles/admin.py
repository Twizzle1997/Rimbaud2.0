from django.contrib import admin
from rimbaud_project.articles.models import Article

@admin.register(Article)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'body')

admin.site.register(Article, AuthorAdmin)
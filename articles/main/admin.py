from django.contrib import admin
from .models import Category, Comment, Article
# Register your models here.

admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Article)
from django.contrib import admin

# Register your models here.
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']

class PostAdmin(admin.ModelAdmin):
    fields = ['category', 'title','body']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

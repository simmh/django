from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category, Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)

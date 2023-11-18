from django.contrib import admin

from blogs.models import Post, Category

admin.site.register(Post)
admin.site.register(Category)

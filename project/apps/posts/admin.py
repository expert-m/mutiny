from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    # model = PostTag
    fields = ('title', 'content', 'created', 'modified', 'tags', 'is_published',)
    list_display = ('title', 'created', 'modified', 'is_published',)
    list_filter = ('created',)
    readonly_fields = ('created', 'modified',)

admin.site.register(Post, PostAdmin)


class PostImageAdmin(admin.ModelAdmin):
    fields = ('image', 'post', 'info', 'created',)
    list_display = ('id', 'info', 'created',)
    list_filter = ('post', 'created',)

admin.site.register(PostImage, PostImageAdmin)

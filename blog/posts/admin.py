from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

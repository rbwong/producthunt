from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('name',  'tagline', 'day', 'discussion_url', 'redirect_url', 'created_at')
admin.site.register(Post, PostAdmin)

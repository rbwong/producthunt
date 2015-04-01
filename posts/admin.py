from django.contrib import admin
from .models import Country, Post


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'short', 'logo_url')
admin.site.register(Country, CountryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'tagline', 'day', 'discussion_url', 'redirect_url', 'created_at', 'is_approved')
admin.site.register(Post, PostAdmin)

from django.contrib import admin

from .models import Tweet


class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user_username', 'user_email']
admin.site.register(Tweet, TweetAdmin)
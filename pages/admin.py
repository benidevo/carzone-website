from django.contrib import admin
from .models.teams import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src='f"{object.avatar.url}"' width="40" style="border-radius: 180%">')
    
    thumbnail.short_description = 'avatar'

    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_at')
    list_display_links = ('id', 'thumbnail', 'first_name')
    search_fields = ('first_name', 'last_name', 'designation')


admin.site.register(Team, TeamAdmin)
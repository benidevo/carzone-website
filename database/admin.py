from django.contrib import admin
from database.models.teams import Team
from database.models.cars import Car
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src='f"{object.avatar.url}"' width="40" style="border-radius: 180%">')
    
    thumbnail.short_description = 'avatar'

    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_at')
    list_display_links = ('id', 'thumbnail', 'first_name')
    search_fields = ('first_name', 'last_name', 'designation')


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src='f"{object.car_image.url}"' width="40" style="border-radius: 100%">')

    thumbnail.short_description = 'car image'

    list_display = ('id', 'thumbnail', 'name', 'model', 'year', 'mileage', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'name')
    search_fields = ('name', 'year', 'model')
    list_editable = ('is_featured',)
    list_filter = ('name', 'year', 'model')

admin.site.register(Team, TeamAdmin)
admin.site.register(Car, CarAdmin)
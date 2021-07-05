from django.contrib import admin
from database.models.teams import Team
from database.models.cars import Car
from database.models.contact import Contact
from database.models.inquiries import Inquiry
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src='f"{object.avatar.url}"' width="40" style="border-radius: 180%">')
    
    thumbnail.short_description = 'avatar'

    list_display = ('thumbnail', 'first_name', 'designation', 'created_at')
    list_display_links = ('thumbnail', 'first_name')
    search_fields = ('first_name', 'last_name', 'designation')


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src='f"{object.car_image.url}"' width="40" style="border-radius: 100%">')

    thumbnail.short_description = 'car image'

    list_display = ('thumbnail', 'name', 'model', 'year', 'mileage', 'is_featured')
    list_display_links = ('thumbnail', 'name')
    search_fields = ('name', 'year', 'model')
    list_editable = ('is_featured',)
    list_filter = ('name', 'year', 'model')

class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'customer_email', 'first_name', 'created_at')
    list_display_links = ('id', 'customer_email', 'first_name')
    search_fields = ('first_name', 'customer_email')

class InquiryAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'name', 'created_at')
    list_display_links = ('id', 'email')
    search_fields = ('name', 'email')

admin.site.register(Team, TeamAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Inquiry, InquiryAdmin)
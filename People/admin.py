from django.contrib import admin

from .models import People

class PeopleAdmin(admin.ModelAdmin):
    model = People
admin.site.register(People, PeopleAdmin)
from django.contrib import admin

from .models import Type

class TypeAdmin(admin.ModelAdmin):
    model = Type
admin.site.register(Type, TypeAdmin)
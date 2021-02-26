from django.contrib import admin

from .models import Selection

class SelectionAdmin(admin.ModelAdmin):
    model = Selection
admin.site.register(Selection, SelectionAdmin)

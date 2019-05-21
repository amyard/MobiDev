from django.contrib import admin
from core.implement.models import UrlModel



@admin.register(UrlModel)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('full_url', 'short_url', 'created', 'modified', )

    fieldsets = (
        ('Url Info', {'fields':('full_url', 'short_url', )}),
        (None, {'fields': ('text', )})
    )
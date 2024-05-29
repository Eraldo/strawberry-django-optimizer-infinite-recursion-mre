from django.contrib import admin

from fruits.models import Color


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from places.models import Place, Image


class ImagePlace(admin.TabularInline):
    model = Image

@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    inlines = [
        ImagePlace,
    ]

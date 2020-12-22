from django.contrib import admin
from places.models import Place, Image


class ImagePlace(admin.TabularInline):
    model = Image


class AdminPlace(admin.ModelAdmin):
    inlines = [
        ImagePlace,
    ]


admin.site.register(Place, AdminPlace)

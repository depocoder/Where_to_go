from django.contrib import admin
from places.models import Place, Image


class AdminPlace(admin.ModelAdmin):
    pass


class ImagePlace(admin.ModelAdmin):
    pass


admin.site.register(Place, AdminPlace)
admin.site.register(Image, ImagePlace)

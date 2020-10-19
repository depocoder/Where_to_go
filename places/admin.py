from django.contrib import admin
from places.models import Place

class AdminPlace(admin.ModelAdmin):
    pass

admin.site.register(Place, AdminPlace)

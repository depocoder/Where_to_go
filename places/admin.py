from django.contrib import admin
from places.models import Place, Image
from django.utils.html import format_html_join


class ImagePlace(admin.TabularInline):
    readonly_fields = ('image_preview',)
    fields = ('image', 'image_preview', 'position')
    def image_preview(self, obj):
        return obj.image_preview
    model = Image

@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    inlines = [
        ImagePlace,
    ]
    
    

from django.contrib import admin
from places.models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin


class ImagePlace(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ('image_preview',)
    fields = ('image', 'image_preview', 'position')

    def image_preview(self, obj):
        return obj.image_preview


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    search_fields = ['title', ]
    inlines = (
        ImagePlace,
    )

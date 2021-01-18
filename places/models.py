from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
from django.utils.html import format_html


class Place(models.Model):
    title = models.CharField('Название места', max_length=100)
    short_description = models.TextField(
        'Короткое описание', null=True, blank=True)
    long_description = HTMLField("Подробное описание", null=True, blank=True)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='')
    place = models.ForeignKey(
        'Place', verbose_name='Место', related_name='image', on_delete=models.CASCADE)
    position = models.PositiveIntegerField('Позиция', default=0)

    @property
    def image_preview(self):
        if self.image:
            return format_html(
                mark_safe('<img src="{}" style="max-height:300px; width:auto">'),
                self.image.url,
                )
        return ""

    class Meta(object):
        ordering = ('position',)

    def __str__(self):
        return f'{self.id} {self.place.title}'

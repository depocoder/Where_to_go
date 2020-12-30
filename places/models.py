from django.db import models
from django.utils.safestring import mark_safe


class Place(models.Model):
    title = models.CharField('Название места', max_length=100)
    description_short = models.CharField('Короткое описание', max_length=100)
    description_long = models.TextField("Подробное описание")
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Изображение', null=True, blank=True, upload_to='')
    place = models.ForeignKey(
        'Place', related_name='place_image', on_delete=models.CASCADE)
    position = models.PositiveIntegerField('Позиция', default=0, blank=False, null=False)

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{url}" width="400" height="300" />'.format(
                url = self.image.url,))
        return ""


    class Meta(object):
        ordering = ['position']
    

    def __str__(self):
        return f'{self.id} {self.place.title}'

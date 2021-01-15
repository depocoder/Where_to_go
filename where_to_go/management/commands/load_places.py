import os
from urllib.parse import urlparse

from django.core.files.base import ContentFile
import requests
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='Json url')

    def handle(self, *args, **kwargs):
        json_url = kwargs['json_url']
        response = requests.get(json_url)
        response.raise_for_status()
        place = response.json()
        place_obj, created = Place.objects.get_or_create(
            title=place['title'],
            description_short=place['description_short'],
            description_long=place['description_long'],
            lat=place['coordinates']['lat'],
            lon=place['coordinates']['lng'],
        )

        for index, image_url in enumerate(place['imgs']):
            image_obj = Image.objects.create(
                place=place_obj,
            )
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            image_content = ContentFile(image_response.content)
            disassembled_url = urlparse(image_url)
            filename, file_ext = os.path.splitext(
                os.path.basename(disassembled_url.path))
            image_obj.image.save(
                f'{place_obj.pk}-{index}.jpg', image_content, save=True)

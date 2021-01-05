import json

from django.shortcuts import render
from places.models import Place
from django.http import HttpResponseNotFound, JsonResponse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def index(request):
    places = []
    for place in Place.objects.all():
        places.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f"place/{place.id}"
            }
        })
    return render(
        request,
        "index.html",
        context={
            'places': json.dumps(places)
        })


def show_place(request, place_id):
    try:
        requested_place = Place.objects.get(id=place_id)
    except (MultipleObjectsReturned, ObjectDoesNotExist):
        return HttpResponseNotFound('<h1>Такой место не найден</h1>')
    images = [image.image.url for image in requested_place.place_image.all()]
    place = {
        'title': requested_place.title,
        'imgs': images,
        "description_short": requested_place.description_short,
        "description_long": requested_place.description_long,
        'coordinates': {
          "lat": requested_place.lat,
          "lng": requested_place.lon
        }
    }
    return JsonResponse(place)

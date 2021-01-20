from django.shortcuts import render
from places.models import Place
from django.http import HttpResponseNotFound, JsonResponse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import get_object_or_404
from django.urls import reverse


def index(request):
    places_serialized = []
    places = Place.objects.all()
    for place in places:
        places_serialized.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place', args=[place.id])
            }
        })
    return render(
        request,
        "index.html",
        context={
            'places': {
                    "type": "FeatureCollection",
                    "features": places_serialized
                    }
        })


def show_place(request, place_id):
    requested_place = get_object_or_404(Place, id=place_id)
    images = [image.image.url for image in requested_place.images.all()]
    place = {
        'title': requested_place.title,
        'imgs': images,
        "description_short": requested_place.short_description,
        "description_long": requested_place.long_description,
        'coordinates': {
          "lat": requested_place.lat,
          "lng": requested_place.lon
        }
    }
    return JsonResponse(place)

from django.shortcuts import render
from places.models import Place


def index(request):
    print(len(Place.objects.all()))
    return render(
        request, "index.html", context={'places': Place.objects.all()})

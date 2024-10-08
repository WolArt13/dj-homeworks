from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_stations = []

    with open(settings.BUS_STATION_CSV, newline="", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            bus_stations.append(row)

    q = request.GET.get('q')
    search_field = request.GET.get('search_field')

    if q and search_field:
        if search_field == 'name':
            search = [station for station in bus_stations if q.lower() in station['Name'].lower()]
        elif search_field == 'street':
            search = [station for station in bus_stations if q.lower() in station['Street'].lower()]
        elif search_field == 'district':
            search = [station for station in bus_stations if q.lower() in station['District'].lower()]
        paginator = Paginator(search, 10)
    else:
        paginator = Paginator(bus_stations, 10)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'bus_stations': page_obj,
        'page': page_obj,
        'total_pages': paginator.num_pages,
        'q': q,
        'search_field': search_field,
    }
    return render(request, 'stations/index.html', context)

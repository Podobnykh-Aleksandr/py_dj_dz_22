from django.shortcuts import render, redirect
from django.urls import reverse
from csv import DictReader
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator


CONTENT = []

with open(BUS_STATION_CSV, encoding='UTF-8') as csvfile:
    CONTENT = [*DictReader(csvfile, delimiter=',', quotechar='"')]
lengthContent = len(CONTENT)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    bus_station = paginator.get_page(page_number)
    page = paginator.get_page(page_number)
    # также передайте в контекст список станций на странице
    context = {
        'bus_stations': bus_station,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

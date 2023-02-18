from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    data_dict = dict()
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_dict[int(row['ID'])] = {'name': row['Name'].replace('«', ''),
                                         'street': row['Street'],
                                         'district': row['District']}
    paginator = Paginator(tuple(data_dict.values()), 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)

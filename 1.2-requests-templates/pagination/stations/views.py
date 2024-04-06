from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(r'C:\Users\Артем\Desktop\dj-homeworks\1.2-requests-templates\pagination\data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        station_list = list(reader)
        paginator = Paginator(station_list, 10)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': station_list,
            'page': page,
        }
    return render(request, 'stations/index.html', context)

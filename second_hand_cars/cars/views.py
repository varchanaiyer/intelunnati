from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404,get_list_or_404
from .models import Car

def home(request):
    cars = Car.objects.all()
    return render(request, 'cars/home.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

def search(request):
    query = request.GET.get('q')
    cars = Car.objects.filter(car_name__icontains=query)
    return render(request, 'cars/search.html', {'cars': cars, 'query': query})

def compare_cars(request):
    car_ids = request.GET.getlist('car_ids')
    if car_ids:
        cars = get_list_or_404(Car, id__in=car_ids)
    else:
        cars = []
    return render(request, 'cars/compare_cars.html', {'cars': cars})

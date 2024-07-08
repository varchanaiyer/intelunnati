from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('search/', views.search, name='search'),
    path('compare/', views.compare_cars, name='compare_cars'),
]

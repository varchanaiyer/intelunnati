import csv
from django.core.management.base import BaseCommand
from cars.models import Car

class Command(BaseCommand):
    help = 'Load cars from CSV file'

    def handle(self, *args, **kwargs):
        with open('D:\gen ai folder\myproject\second_hand_cars.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                car = Car(
                    company_name=row['Company Name'],
                    car_name=row['Car Name'],
                    variant=row['Variant'],
                    fuel_type=row['Fuel Type'],
                    tyre_condition=row['Tyre Condition'],
                    make_year=row['Make Year'],
                    owner_type=row['Owner Type'],
                    registration_number=row['Registration Number'],
                    mileage=row['Mileage'],
                    price=row['Price'],
                    transmission_type=row['Transmission Type'],
                    body_color=row['Body Color'],
                    service_record=row['Service Record'],
                    insurance=row['Insurance'],
                    registration_certificate=row['Registration Certificate'],
                    accessories=row['Accessories'],
                )
                car.save()

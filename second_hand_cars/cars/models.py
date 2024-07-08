from django.db import models

class Car(models.Model):
    company_name = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    variant = models.CharField(max_length=100, null=True, blank=True)
    fuel_type = models.CharField(max_length=50)
    tyre_condition = models.CharField(max_length=50)
    make_year = models.IntegerField()
    owner_type = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50)
    mileage = models.IntegerField()
    price = models.IntegerField()
    transmission_type = models.CharField(max_length=50)
    body_color = models.CharField(max_length=50)
    service_record = models.TextField()
    insurance = models.CharField(max_length=100)
    registration_certificate = models.CharField(max_length=50)
    accessories = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.company_name} {self.car_name} ({self.make_year})"

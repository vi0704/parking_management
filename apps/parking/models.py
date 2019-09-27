from django.db import models


class Parking(models.Model):
    car_colour = models.CharField(max_length=255)
    car_number = models.CharField(max_length=255)
    is_parked = models.BooleanField(default=False)
    last_entry = models.DateTimeField(auto_now=True)



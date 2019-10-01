from django.core.management.base import BaseCommand
from django.core import management
from parking.models import Parking
from django.core.exceptions import ObjectDoesNotExist
from .validations import is_vehicle_number, is_color


def park():
    colour = input('Enter the colour of vehicle : ')
    colour = is_color(colour)
    number = input('Enter the vehicle number : ')
    number = is_vehicle_number(number)
    print(colour, number)

    try:
        parking = Parking.objects.get(car_number=number)
        parking.car_colour = colour
        parking.is_parked = True
        parking.save()
        print('************************************************')
        print('car number {} successfully parked'.format(number))
        print('************************************************')

    except ObjectDoesNotExist:
        Parking.objects.create(car_number=number, car_colour=colour, is_parked=True)
        print('************************************************')
        print('car number {} successfully parked'.format(number))
        print('************************************************')

    return management.call_command('parking')


class Command(BaseCommand):
    def handle(self, **options):
        park()

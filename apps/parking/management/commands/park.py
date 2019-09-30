from django.core.management.base import BaseCommand
from django.core import management
from parking.models import Parking
from django.core.exceptions import ObjectDoesNotExist
import re


def is_color(string):
    if re.match(r'^[a-zA-Z ]*$', string):
        if not string.isspace() and string != '':
            pass
        else:
            colour = input('invalid color name please give correct input : ')
            return is_color(colour)
    else:
        colour = input('invalid color name please give correct input : ')
        return is_color(colour)
    return string


def is_vehicle_number(string):
    if string.isalnum():
        pass
    else:
        number = input('invalid number please give correct input : ')
        return is_vehicle_number(number)
    return string


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

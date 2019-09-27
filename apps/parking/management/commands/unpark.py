from django.core.management.base import BaseCommand
from datetime import datetime
from django.core import management
from parking.models import Parking
from django.core.exceptions import ObjectDoesNotExist


def is_empty(string, property):
    if string and string.strip():
        pass
    else:
        print('Invalid entry provide some valid input')
        colour = input('Enter the {} of vechicle'.format(property))
        return is_empty(colour, property)


def unpark():
    number = input('Enter the vehicle number  ')
    is_empty(number, 'number')

    try:
        parking = Parking.objects.get(car_number=number)
        print(parking)
        if parking.is_parked:
            parking.is_parked = False
            print('car number {} successfully unparked'.format(number))
        else:
            print('car number {} is not parked'.format(number))
        parking.save()


    except ObjectDoesNotExist:
        print('car number {} is not parked'.format(number))

    management.call_command('parking')


class Command(BaseCommand):
    def handle(self, **options):
        unpark()

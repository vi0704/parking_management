from django.core.management.base import BaseCommand
from datetime import datetime
from django.core import management
from parking.models import Parking
from django.core.exceptions import ObjectDoesNotExist
from parking.management.commands.park import is_vehicle_number


def unpark():
    number = input('Enter the vehicle number to unpark : ')
    number=is_vehicle_number(number)

    try:
        parking = Parking.objects.get(car_number=number)
        print('**************************************')
        if parking.is_parked:
            parking.is_parked = False
            print('car number {} successfully unparked'.format(number))
        else:
            print('car number {} is not parked'.format(number))
            print('**************************************')
            return unpark()
        print('**************************************')
        parking.save()


    except ObjectDoesNotExist:
        print('**************************************')
        print('car number {} is not parked'.format(number))
        print('**************************************')
        return unpark()

    management.call_command('parking')


class Command(BaseCommand):
    def handle(self, **options):
        unpark()

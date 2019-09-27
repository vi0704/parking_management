from django.core.management.base import BaseCommand
from django.core import management
from parking.models import Parking
from django.core.exceptions import ObjectDoesNotExist


def is_empty(string, field):
    if string and string.strip() and string!='':
        pass
    else:
        print('Invalid entry provide some valid input')
        colour = input('Enter the {} of vehicle'.format(field))
        return is_empty(colour, field)

def is_colour(string, field):
    if string.isalpha() or string==' ':
        pass
    else:
        print('Invalid colour name ')
        colour = input('Enter the {} of vehicle'.format(field))
        is_empty(colour, field)
        return is_colour(colour,field)



def park():
    colour = input('Enter the colour of vehicle : ')
    is_empty(colour, 'colour')
    is_colour(colour, 'colour')
    number = input('Enter the vehicle number : ')
    is_empty(colour, 'number')

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

from django.core.management.base import BaseCommand
from datetime import datetime
from django.core import management
from parking.models import Parking
from django.core.exceptions import ObjectDoesNotExist


def is_empty(string,property):
    if string and string.strip():
        pass
    else:
        print('Invalid entry provide some valid input')
        colour=input('Enter the {} of vechicle'.format(property))
        return is_empty(colour, property)

def park():
    colour=input('Enter the colour of vechicle  ')
    is_empty(colour, 'colour')
    number=input('Enter the vehicle number  ')
    is_empty(colour, 'number')

    try:
        parking=Parking.objects.get(car_number=number)
        print(parking)
        parking.is_parked = True
        parking.save()
        print('car number {} successfully parked'.format(number))

    except ObjectDoesNotExist:
        Parking.objects.create(car_number=number, car_colour=colour)
        print('car number {} successfully parked'.format(number))


    with open('parking/management/commands/command.txt') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    print('Here is the list of all available actions')
    content = [x.strip() for x in content]
    print(content)
    # task = True
    management.call_command('parking')
    # while task:
    #
    #     action = input('please type the name of action you want to perform ')
    #     if action in content:
    #         management.call_command(action)
    #     else:
    #         a = input('unavailable action please type 1 to try again or any other key  to leave ')
    #         if a == '1':
    #             task = True
    #         else:
    #
    #             print('thanks of using the service')
    #             task = False
    #             return 'good bye'

    # management.call_command('park')


class Command(BaseCommand):
    def handle(self, **options):
        park()

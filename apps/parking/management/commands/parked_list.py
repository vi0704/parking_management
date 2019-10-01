from django.core.management.base import BaseCommand
from django.core import management
from parking.models import Parking


def parked_list():
    list = Parking.objects.filter(is_parked=True)
    print('************* parked vehicles ***************')
    if len(list) > 0:
        for vehicle in list:
            print(vehicle.car_number)
        print('*********************************************')
    else:
        print('There is not any vehicle parked')
        print('**********************************************')

    management.call_command('parking')


class Command(BaseCommand):
    def handle(self, **options):
        parked_list()

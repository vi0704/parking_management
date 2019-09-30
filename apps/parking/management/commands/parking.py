from django.core.management.base import BaseCommand
from django.core import management
from datetime import datetime


def update_blog():
    with open('parking/management/commands/command.txt') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    print('Here is the list of all available actions')
    content = [x.strip() for x in content]
    print(content)
    # task = True
    # while task:

    action = input('please type the name of action you want to perform :')
    if action in content:
        management.call_command(action)
    else:
        print('unavailable action please select from the given option or ctrl+c to exit')
        update_blog()


class Command(BaseCommand):
    def handle(self, **options):
        update_blog()

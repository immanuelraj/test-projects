from cycle.models import HandleBarWithBrake
from django.core.management import BaseCommand
from . import purchase_cycle

class Command(BaseCommand):

    def create_handle_bar_with_brake(self):
        while True:
            try:
                handle_bar_with_brake_count=int(input("Enter Number of HandleBarWithBrake to be created: "))
                break
            except ValueError:
                print ('Invalid Input. Enter the integer value')
        for _ in range(handle_bar_with_brake_count):
            data = purchase_cycle.get_input()
            HandleBarWithBrake.objects.create(**data)

    def handle(self, *args, **options):
        print('Start create HandleBarWithBrake')
        self.create_handle_bar_with_brake()
        print('Creating HandleBarWithBrake are completed')
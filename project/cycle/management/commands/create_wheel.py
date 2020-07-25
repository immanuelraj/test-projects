import random
from cycle.models import Wheel
from django.core.management import BaseCommand
from . import purchase_cycle

class Command(BaseCommand):

    def create_wheel(self):
        while True:
            try:
                wheel_count=int(input("Enter Number of Wheel to be created: "))
                break
            except ValueError:
                print ('Invalid Input. Enter the integer value')
        for _ in range(wheel_count):
            data = purchase_cycle.get_input()
            data['tyre_type'] = random.choice(purchase_cycle.tube)
            data['spoke_price'] = random.choice(purchase_cycle.price)
            data['rim_price'] = random.choice(purchase_cycle.price)
            data['tube_price'] = random.choice(purchase_cycle.price)
            data['tyre_price'] = random.choice(purchase_cycle.price)
            Wheel.objects.create(**data)

    def handle(self, *args, **options):
        print('Start create Wheel')
        self.create_wheel()
        print('Creating Wheel are completed')
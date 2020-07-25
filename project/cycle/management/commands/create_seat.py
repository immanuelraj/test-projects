from cycle.models import Seating
from django.core.management import BaseCommand
from . import purchase_cycle

class Command(BaseCommand):
    
    def create_seating(self):
        while True:
            try:
                seating_count=int(input("Enter Number of Seating to be created: "))
                break
            except ValueError:
                print ('Invalid Input. Enter the integer value')
        for _ in range(seating_count):
            data = purchase_cycle.get_input()
            Seating.objects.create(**data)

    def handle(self, *args, **options):
        print('Start create Seating')
        self.create_seating()
        print('Creating Seating are completed')
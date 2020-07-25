from cycle.models import Frame
from django.core.management import BaseCommand
from . import purchase_cycle

class Command(BaseCommand):

    def create_frame(self):
        while True:
            try:
                frame_count=int(input("Enter Number of Frame to be created: "))
                break
            except ValueError:
                print ('Invalid Input. Enter the integer value')
        for _ in range(frame_count):
            data = purchase_cycle.get_input()
            Frame.objects.create(**data)

    def handle(self, *args, **options):
        print('Start create Frames')
        self.create_frame()
        print('Creating frames are completed')
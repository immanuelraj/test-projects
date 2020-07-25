import random
import datetime
import string
import concurrent.futures
from cycle.models import Frame, HandleBarWithBrake, Seating, Wheel, ChainAssembly, Cycle
from django.core.management import BaseCommand

tube = ('Tube Less','Tube')
price = (56.45, 53.23, 64.33, 43.24, 43.43, 43.53, 42.23, 63.53, 76.65, 76.56, 89.76, 54.45, 65.56,)

def get_input():
    while True:
        try:
            model_no=int(input("Enter the Model No: "))
            break
        except ValueError:
            print ('Invalid Input. Enter the integer value')
    while True:
        try:
            name=str(input("Enter the Name: "))
            break
        except ValueError:
            print ('Invalid Input')
    while True:
        try:
            price_from=str(input("Enter the Price From (eg: 2015-01-01): "))
            break
        except ValueError:
            print ('Invalid Input')
    while True:
        try:
            price_to=str(input("Enter the Price To (eg: 2015-01-01):"))
            break
        except ValueError:
            print ('Invalid Input')
    while True:
        try:
            price=float(input("Enter the Price: "))
            break
        except ValueError:
            print ('Invalid Input. Enter the float value')

    return {'model_no': model_no, 'name' : name , 'price_from' : price_from, 'price_to' : price_to, 'price' : price}


class Command(BaseCommand):

    def create_frame(self):
        while True:
            try:
                frame_count=int(input("Enter Number of Frame to be created: "))
                break
            except ValueError:
                print ('Invalid Input. Enter the integer value')
        for _ in range(frame_count):
            data = get_input()
            Frame.objects.create(**data)

    def create_handle_bar_with_brake(self):
        while True:
            try:
                handle_bar_with_brake_count=int(input("Enter Number of HandleBarWithBrake to be created: "))
                break
            except ValueError:
                print ('Invalid Input. Enter the integer value')
        for _ in range(handle_bar_with_brake_count):
            data = get_input()
            HandleBarWithBrake.objects.create(**data)
    
    def create_seating(self):
        while True:
            try:
                seating_count=int(input("Enter Number of Seating to be created: "))
                break
            except ValueError:
                print ('Invalid Input. Enter the integer value')
        for _ in range(seating_count):
            data = get_input()
            Seating.objects.create(**data)
    
    def create_wheel(self):
        while True:
            try:
                wheel_count=int(input("Enter Number of Wheel to be created: "))
                break
            except ValueError:
                print ('Invalid Input. Enter the integer value')
        for _ in range(wheel_count):
            data = get_input()
            data['tyre_type'] = random.choice(self.tube)
            data['spoke_price'] = random.choice(self.price)
            data['rim_price'] = random.choice(self.price)
            data['tube_price'] = random.choice(self.price)
            data['tyre_price'] = random.choice(self.price)
            Wheel.objects.create(**data)

    def create_chain_assembly(self):
        while True:
            try:
                chain_assembly_count=int(input("Enter Number of ChainAssembly to be created: "))
                break
            except ValueError:
                print ('Invalid Input. Enter the integer value')
        for _ in range(chain_assembly_count):
            data = get_input()
            ChainAssembly.objects.create(**data)

    def create_cycle(self):

        frame_names = ', '.join(name[0] for name in Frame.objects.all().values_list('name'))
        handle_bar_names = ', '.join(name[0] for name in HandleBarWithBrake.objects.all().values_list('name'))
        seating_names = ', '.join(name[0] for name in Seating.objects.all().values_list('name'))
        wheel_names = ', '.join(name[0] for name in Wheel.objects.all().values_list('name'))
        chain_names = ', '.join(name[0] for name in ChainAssembly.objects.all().values_list('name'))
        print('Select the frame for the cycle ({0}): '.format(frame_names), end="")
        frame = str(input())
        print('Select the HandleBarWithBrake for the cycle ({0}): '.format(handle_bar_names), end="")
        handlebar_with_brake = str(input())
        print('Select the Seating for the cycle ({0}): '.format(seating_names), end="")
        seating = str(input())
        print('Select the Wheel for the cycle ({0}): '.format(wheel_names), end="")
        wheel = str(input())
        print('Select the ChainAssembly for the cycle ({0}): '.format(chain_names), end="")
        chain_assembly = str(input())
        cycle = Cycle.objects.create(frame=Frame.objects.filter(name__icontains=frame).first(),
                                    handlebar_with_brake=HandleBarWithBrake.objects.filter(name__icontains=handlebar_with_brake).first(),
                                    seating=Seating.objects.filter(name__icontains=seating).first(),
                                    wheel=Wheel.objects.filter(name__icontains=wheel).first(),
                                    chain_assembly=ChainAssembly.objects.filter(name__icontains=chain_assembly).first())
        return cycle.price

    def handle(self, *args, **options):
        print('Start Purchasing Cycle')
        self.create_frame()
        self.create_handle_bar_with_brake()
        self.create_seating()
        self.create_wheel()
        self.create_chain_assembly()
        price_list = []
        with concurrent.futures.ThreadPoolExecutor() as execution:
            result = []
            while True:
                try:
                    cycles_count=int(input("Enter Number of Cycle to be created: "))
                    break
                except ValueError:
                    print ('Invalid Input. Enter the integer value')
            for count in range(cycles_count):
                result.append(execution.submit(self.create_cycle))
                if count % 10 == 0:
                    for f in concurrent.futures.as_completed(result):
                        price_list.append(f.result())
                        result = []
            for f in concurrent.futures.as_completed(result):
                price_list.append(f.result())
        print('Purchasing Cycle completed')
        print('Price for {0} cycles are {1}'.format(cycles_count, sum(price_list)))
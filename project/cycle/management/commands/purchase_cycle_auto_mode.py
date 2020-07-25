import random
import string
import concurrent.futures
from cycle.models import Frame, HandleBarWithBrake, Seating, Wheel, ChainAssembly, Cycle
from django.core.management import BaseCommand

class Command(BaseCommand):

    frame_names = ('Steel Frame','Fiber Frame','Metal frame',)
    handle_bar_names = ('Steel Handle Bar With brake','Steel Handle Bar With disk brake',)
    seating_names = ('Racing Seat', 'Comfort Seat', 'Male Seat', 'Female',)
    wheel_names = ('Clincher Wheels', 'Tubular Wheels', 'Tubeless Wheels',)
    chain_names = ('Single Speed', 'Fixed Gears', 'Hub Gears', 'Derailleur Gears', 'Five Speed',)
    tube = ('Tube Less','Tube',)
    from_ = ( "2015-01-01", "2016-01-31", "2017-01-01", "2014-01-31",)
    to = ("2018-01-01", "2019-01-31", "2020-01-01", "2021-01-31",)
    price = (56.45, 53.23, 64.33, 43.24, 43.43, 43.53, 42.23, 63.53, 76.65, 76.56, 89.76, 54.45, 65.56,)

    def generate_id(length=10):
        return int(''.join(random.choice(string.digits) for i in range(5)))

    def get_input(self):
        return {'model_no': self.generate_id(), 'price_from' : random.choice(self.from_), 'price_to' : random.choice(self.to), 'price' : random.choice(self.price)}

    def create_frame(self):
        for _ in range(6):
            data = self.get_input()
            data['name'] = random.choice(self.frame_names),
            Frame.objects.create(**data)

    def create_handle_bar_with_brake(self):
        for _ in range(6):
            data = self.get_input()
            data['name'] = random.choice(self.handle_bar_names),
            HandleBarWithBrake.objects.create(**data)
    
    def create_seating(self):
        for _ in range(6):
            data = self.get_input()
            data['name'] = random.choice(self.seating_names),
            Seating.objects.create(**data)
    
    def create_wheel(self):
        for _ in range(6):
            data = self.get_input()
            data['name'] = random.choice(self.wheel_names)
            data['tyre_type'] = random.choice(self.tube)
            data['spoke_price'] = random.choice(self.price)
            data['rim_price'] = random.choice(self.price)
            data['tube_price'] = random.choice(self.price)
            data['tyre_price'] = random.choice(self.price)
            Wheel.objects.create(**data)

    def create_chain_assembly(self):
        for _ in range(6):
            data = self.get_input()
            data['name'] = random.choice(self.chain_names),
            ChainAssembly.objects.create(**data)

    def create_cycle(self):
        cycle = Cycle.objects.create(frame=Frame.objects.get(id=random.randint(1, 5)),
                                    handlebar_with_brake=HandleBarWithBrake.objects.get(id=random.randint(1, 5)),
                                    seating=Seating.objects.get(id=random.randint(1, 5)),
                                    wheel=Wheel.objects.get(id=random.randint(1, 5)),
                                    chain_assembly=ChainAssembly.objects.get(id=random.randint(1, 5)))
        return cycle.price

    def add_arguments(self, parser):
        parser.add_argument('number_of_cycle', type=int, help='eg. 1000')

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
            for count in range(options['number_of_cycle']):
                result.append(execution.submit(self.create_cycle))
                if count % 10 == 0:
                    for f in concurrent.futures.as_completed(result):
                        price_list.append(f.result())
                        result = []
            for f in concurrent.futures.as_completed(result):
                price_list.append(f.result())
        print('Purchasing Cycle completed')
        print('Price for {0} cycles are {1}'.format(options['number_of_cycle'], sum(price_list)))
from cycle.models import ChainAssembly
from django.core.management import BaseCommand
from . import purchase_cycle

class Command(BaseCommand):

    def create_chain_assembly(self):
        while True:
            try:
                chain_assembly_count=int(input("Enter Number of ChainAssembly to be created: "))
                break
            except ValueError:
                print ('Invalid Input. Enter the integer value')
        for _ in range(chain_assembly_count):
            data = purchase_cycle.get_input()
            ChainAssembly.objects.create(**data)

    def handle(self, *args, **options):
        print('Start create ChainAssembly')
        self.create_chain_assembly()
        print('Creating ChainAssembly are completed')
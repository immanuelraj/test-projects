from django.db import models
from . import generate
from django.conf import settings


class Frame(models.Model):
    model_no = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    price_from = models.DateField()
    price_to = models.DateField()
    price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    ext_id = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.name, str(self.model_no))

    def check_unique(self, ext_id):
        return not Frame.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate.generate_unique_ext(self, 10)
        super(Frame, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']


class HandleBarWithBrake(models.Model):
    model_no = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    price_from = models.DateField()
    price_to = models.DateField()
    price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    ext_id = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.name, str(self.model_no))

    def check_unique(self, ext_id):
        return not HandleBarWithBrake.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate.generate_unique_ext(self, 10)
        super(HandleBarWithBrake, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']


class Seating(models.Model):
    model_no = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    price_from = models.DateField()
    price_to = models.DateField()
    price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    ext_id = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.name, str(self.model_no))

    def check_unique(self, ext_id):
        return not Seating.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate.generate_unique_ext(self, 10)
        super(Seating, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']


class Wheel(models.Model):

    TYPES = (('Tube Less', 'Tube Less'), ('Tube', 'Tube'))
    model_no = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    price_from = models.DateField()
    price_to = models.DateField()
    spoke_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    rim_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    tube_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    tyre_price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    tyre_type = models.CharField(max_length=10, choices=TYPES)
    price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    ext_id = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.name, str(self.model_no))

    def check_unique(self, ext_id):
        return not Wheel.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate.generate_unique_ext(self, 10)
            self.price = sum([self.spoke_price , self.rim_price , self.tube_price , self.tyre_price])
        super(Wheel, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']

class ChainAssembly(models.Model):
    model_no = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    price_from = models.DateField()
    price_to = models.DateField()
    price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    ext_id = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.name, str(self.model_no))

    def check_unique(self, ext_id):
        return not ChainAssembly.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate.generate_unique_ext(self, 10)
        super(ChainAssembly, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']


class Cycle(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    handlebar_with_brake = models.ForeignKey(HandleBarWithBrake, on_delete=models.CASCADE)
    seating = models.ForeignKey(Seating, on_delete=models.CASCADE)
    wheel = models.ForeignKey(Wheel, on_delete=models.CASCADE)
    wheel_unit = models.PositiveIntegerField(default=2)
    chain_assembly = models.ForeignKey(ChainAssembly, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    ext_id = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} {1} {2} {3} {4} Cycle'.format(self.chain_assembly.name, self.wheel.name, self.seating.name, self.frame.name, self.handlebar_with_brake.name)

    def check_unique(self, ext_id):
        return not Cycle.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate.generate_unique_ext(self, 10)
            self.price = sum([self.frame.price , self.handlebar_with_brake.price , self.seating.price , (self.wheel.price * self.wheel_unit)  , self.chain_assembly.price])
        super(Cycle, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
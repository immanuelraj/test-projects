from django.contrib import admin
from .models import Frame, HandleBarWithBrake, Seating, Wheel, ChainAssembly, Cycle


admin.site.register(Frame)
admin.site.register(HandleBarWithBrake)
admin.site.register(Seating)
admin.site.register(Wheel)
admin.site.register(ChainAssembly)
admin.site.register(Cycle)
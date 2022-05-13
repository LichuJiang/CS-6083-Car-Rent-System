from django.contrib import admin

# Register your models here.
#from .models import LxyClass 
#admin.site.register(LxyClass)

from .models import LxyCustomer
admin.site.register(LxyCustomer)

from .models import LxyOffice
admin.site.register(LxyOffice)

from .models import LxyRentServ
admin.site.register(LxyRentServ)

from .models import LxyVehicle
admin.site.register(LxyVehicle)
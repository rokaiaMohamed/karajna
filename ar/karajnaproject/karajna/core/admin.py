from django.contrib import admin
from .models import Brand
from .models import Version
from .models import Car 


admin.site.register(Car)

admin.site.register(Version)
admin.site.register(Brand)
#admin.site.register(Price)

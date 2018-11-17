import django_filters
from .models import Car , Range
from django import forms

class CarFilter(django_filters.FilterSet):
    
    class Meta:
        model = Car
        fields = {
            'brand': ['exact', ],
            'version': ['exact', ],
            'price': [ 'lte' ,],
            'distance': [ 'lte', ],
            'production_date': [ 'gte',],
            'fuel_type': ['exact', ],
            'car_body': ['exact', ],
        }
    def __init__(self, *args, **kwargs):
        super(CarFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()
      
        
        #fields = ['brand', 'version', 'price', 'distance' , 'production_date' , 'fuel_type' , 'car_body']

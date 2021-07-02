from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField 
from database.models.choices import *

class Car(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=255)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=80)
    year = models.IntegerField(('year'), choices=year_choices)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=200)
    miles = models.IntegerField()
    doors = models.CharField(choices= door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=150)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    added_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

import uuid
from django.db import models
from datetime import datetime

class Contact(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_id = models.CharField(blank=True, max_length=255)
    customer_need = models.CharField(max_length=255)
    customer_email = models.EmailField()
    phone = models.CharField(max_length=255)
    customer_city = models.CharField(max_length=255)
    customer_state = models.CharField(max_length=255)
    car_id = models.CharField(max_length=255)
    car_name = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(blank=True, default=datetime.now)


    def __str__(self):
        return self.customer_email
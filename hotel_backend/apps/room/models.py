from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Room(models.Model):

    categories = [
        ('single','single'),
        ('double', 'double'),
        ('twin', 'twin'),
        ('suite', 'suite')
    ]

    image = CloudinaryField('img', blank=False, null=False)

    capacity = models.IntegerField('capacity', blank=False, null=False, db_index=True, default=0,choices=categories)

    occupied = models.BooleanField('occupied', null=False, blank=False, db_index=True)

    price = models.IntegerField('price', blank=False, null=False, default=0) 

    room_type = models.CharField('room_type', null=False, blank=False, choices=categories, max_length=15)

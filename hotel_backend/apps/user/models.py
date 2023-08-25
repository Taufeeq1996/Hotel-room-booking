from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):

    first_name = models.CharField('first_name', max_length=15, blank=False, null=False, db_index=True)

    last_name = models.CharField('last_name', max_length=15, blank=True, null = False, db_index=True)

    age = models.PositiveIntegerField('age', default=0, blank=False, null=False)

    email = models.EmailField('email', max_length=50, blank=False, null=False, db_index=True)

    phone = models.CharField('phone', max_length=15, blank=False, null=False)

    created_at = models.DateTimeField('created_at', default=timezone.now)

    gender = models.CharField('gender', blank=False, null=False, choices=(('Male','Male'),('Female','Female')), max_length=10)

    print(first_name)



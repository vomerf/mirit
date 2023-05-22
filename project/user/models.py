from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    class Status(models.TextChoices):
        CUSTOMER = 'CUSTOMER', 'customer'
        PERFOMER = 'PERFOMER', 'perfomer'
    birth_date = models.DateField('Birthday', blank=True)
    status = models.CharField(
        'User status',
        max_length=max((len(v) for v in Status.values)),
        choices=Status.choices
    )
    middle_name = models.CharField('Middle name', max_length=50)

    def __str__(self):
        return str(self.username)

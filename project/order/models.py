from django.core.exceptions import ValidationError
from django.db import models

from user.models import Profile


class Order(models.Model):
    text = models.CharField(max_length=500)
    pub_date = models.DateField(auto_now=True)
    customer = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='customer_order'
    )
    perfomer = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, related_name='perfomer_order'
    )
    accepted = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)


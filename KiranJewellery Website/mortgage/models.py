from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Mortgage(models.Model):
    date_of_transaction = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    item = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=4, decimal_places=3)
    rate = models.DecimalField(max_digits=4, decimal_places=3)
    principle = models.DecimalField(max_digits=19, decimal_places=3)
    interest = models.DecimalField(max_digits=8, decimal_places=3)
    amount = models.DecimalField(max_digits=19, decimal_places=3)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mortgage-detail', kwargs={'pk' : self.pk})



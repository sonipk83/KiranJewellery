from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Purchase(models.Model):
    date_of_transaction = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    actual_weight = models.DecimalField(max_digits=4, decimal_places=3)
    deduction = models.DecimalField(max_digits=4, decimal_places=3)
    rate = models.DecimalField(max_digits=19, decimal_places=3)
    net_weight = models.DecimalField(max_digits=19, decimal_places=3)
    amount = models.DecimalField(max_digits=19, decimal_places=3)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

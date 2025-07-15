from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Transaction(models.Model):
    INCOME  = 'income'
    EXPENSE = 'expense'
    TYPE_CHOICES = [
        (INCOME,  'درآمد'),
        (EXPENSE, 'هزینه'),
    ]

    type        = models.CharField(max_length=7, choices=TYPE_CHOICES)
    amount      = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    category    = models.CharField(max_length=50)
    date        = models.DateField()

    def __str__(self):
        return f"{self.description} - {self.amount}"

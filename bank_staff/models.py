from django.db import models

from decimal import Decimal

# Create your models here.


class Bank(models.Model):
    total_funds = models.DecimalField(max_digits=19, decimal_places=2)

    @classmethod
    def add_funds(cls, amount: Decimal):
        bank = cls.objects.get(pk=1)
        bank.total_funds += amount
        bank.save()

    @classmethod
    def remove_funds(cls, amount: Decimal):
        bank = cls.objects.get(pk=1)
        bank.total_funds -= amount
        bank.save()

    @classmethod
    def is_sufficient(cls, amount: Decimal):
        bank = cls.objects.get(pk=1)
        return bank.total_funds >= amount


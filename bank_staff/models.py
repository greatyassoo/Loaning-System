from django.db import models

# Create your models here.


class Bank(models.Model):
    total_funds = models.DecimalField(max_digits=19, decimal_places=2)

    @classmethod
    def add_funds(cls, amount: float):
        bank = cls.objects.get(pk=1)
        bank.total_funds += amount
        bank.save()

    @classmethod
    def remove_funds(cls, amount: float):
        bank = cls.objects.get(pk=1)
        bank.total_funds -= amount
        bank.save()

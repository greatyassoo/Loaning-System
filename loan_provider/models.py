from django.conf import settings
from django.db import models
from .enums import Status

# Create your models here.


class LoanFundApplication(models.Model):
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=Status,
        default=Status.PENDING
    )
    loan_provider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

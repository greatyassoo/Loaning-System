from django.conf import settings
from django.db import models

from loan_provider.enums import Status

# Create your models here.


class LoanApplication(models.Model):
    amount = models.FloatField()
    status = models.CharField(
        max_length=10,
        choices=Status,
        default=Status.PENDING
    )

    # very bad code smell, I should probably extend the user entity into 2 separate classes
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class Loan(models.Model):
    amount = models.FloatField()
    interest_rate = models.FloatField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class Payment(models.Model):
    amount = models.FloatField()
    loan = models.ForeignKey(
        "loan_customer.Loan",
        on_delete=models.CASCADE
    )

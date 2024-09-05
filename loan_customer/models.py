from django.conf import settings
from django.db import models

from loan_provider.enums import Status

# Create your models here.


class LoanApplication(models.Model):
    amount = models.DecimalField(max_digits=19, decimal_places=2)
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
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=3, decimal_places=2)  # eg: 0.1, 0.22
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class Payment(models.Model):
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    loan = models.ForeignKey(
        "loan_customer.Loan",
        on_delete=models.CASCADE
    )

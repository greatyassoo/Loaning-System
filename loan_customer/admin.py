from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Loan)
admin.site.register(models.LoanApplication)
admin.site.register(models.Payment)

from django.db import models


class Status(models.TextChoices):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DENIED = "DENIED"

from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser
from django.db import models
from .auth_enums import UserRole


class BearerToken(TokenAuthentication):
    keyword = 'Bearer'


class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=[(tag, tag.value) for tag in UserRole],
        default=UserRole.LOAN_CUSTOMER,
        null=False
    )

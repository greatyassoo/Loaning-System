from rest_framework import serializers
from .models import Bank

from loan_provider.models import LoanFundApplication

from authentication.models import CustomUser


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['total_funds',]


class UsernameIDCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']


class BankLoanFundApplicationSerializer(serializers.ModelSerializer):
    loan_provider = UsernameIDCustomUserSerializer(read_only=True)

    class Meta:
        model = LoanFundApplication
        fields = ['id', 'amount', 'status', 'loan_provider']

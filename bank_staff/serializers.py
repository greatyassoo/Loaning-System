from rest_framework import serializers
from .models import Bank

from loan_provider.models import LoanFundApplication

from authentication.models import CustomUser

from loan_customer.models import LoanApplication, Loan


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['total_funds',]


class UsernameIDCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']


class BankStaffLoanFundApplicationSerializer(serializers.ModelSerializer):
    loan_provider = UsernameIDCustomUserSerializer(read_only=True)

    class Meta:
        model = LoanFundApplication
        fields = ['id', 'amount', 'status', 'loan_provider']


class BankStaffLoanApplicationSerializer(serializers.ModelSerializer):
    customer = UsernameIDCustomUserSerializer(read_only=True)

    class Meta:
        model = LoanApplication
        fields = ['id', 'amount', 'status', 'customer']


class LoanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['interest_rate', 'end_date']


class LoanListSerializer(serializers.ModelSerializer):
    customer = UsernameIDCustomUserSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = ['id', 'amount', 'interest_rate', 'start_date', 'end_date', 'customer']

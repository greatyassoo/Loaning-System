from rest_framework import serializers

from .models import LoanApplication
from .models import Loan
from .models import Payment


class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = ['id', 'amount', 'status']
        read_only_fields = ['customer']


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id', 'amount', 'interest_rate', 'start_date', 'end_date', 'customer']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'loan']

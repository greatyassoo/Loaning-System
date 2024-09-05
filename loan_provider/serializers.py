from rest_framework import serializers
from .models import LoanFundApplication


class LoanFundApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanFundApplication
        fields = ['id', 'amount', 'status']
        read_only_fields = ['loan_provider']

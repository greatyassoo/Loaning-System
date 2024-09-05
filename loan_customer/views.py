from rest_framework import generics

from . import models
from . import serializers

# Create your views here.


class LoanApplicationListCreate(generics.ListCreateAPIView):
    queryset = models.LoanApplication.objects.all()
    serializer_class = serializers.LoanApplicationSerializer


class LoanListCreate(generics.ListCreateAPIView):
    queryset = models.Loan.objects.all()
    serializer_class = serializers.LoanSerializer


class PaymentListCreate(generics.ListCreateAPIView):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


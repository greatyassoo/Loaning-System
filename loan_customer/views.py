from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from authentication.permissions import IsLoanCustomer
from authentication.models import BearerToken

from . import models
from . import serializers

# Create your views here.


class BaseCustomerView:
    authentication_classes = [SessionAuthentication, BearerToken]
    permission_classes = [IsAuthenticated, IsLoanCustomer]


class LoanApplicationListCreate(BaseCustomerView, generics.ListCreateAPIView):
    queryset = models.LoanApplication.objects.all()
    serializer_class = serializers.LoanApplicationSerializer

    def get_queryset(self):
        return models.LoanApplication.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class LoanList(BaseCustomerView, generics.ListAPIView):
    queryset = models.Loan.objects.all()
    serializer_class = serializers.LoanSerializer

    def get_queryset(self):
        return models.Loan.objects.filter(customer=self.request.user)


class PaymentListCreate(BaseCustomerView, generics.ListCreateAPIView):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


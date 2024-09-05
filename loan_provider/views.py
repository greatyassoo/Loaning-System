from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsLoanProvider
from rest_framework.authentication import SessionAuthentication
from authentication.models import BearerToken

from .models import LoanFundApplication
from .serializers import LoanFundApplicationSerializer


class LoanFundApplicationListCreate(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BearerToken]
    permission_classes = [IsAuthenticated, IsLoanProvider]
    serializer_class = LoanFundApplicationSerializer

    def get_queryset(self):
        return LoanFundApplication.objects.filter(loan_provider=self.request.user)

    def perform_create(self, serializer):
        serializer.save(loan_provider=self.request.user)

from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from authentication.permissions import IsBankStaff
from authentication.models import BearerToken

from .serializers import BankSerializer, BankStaffLoanFundApplicationSerializer
from .models import Bank
from . import services

from loan_provider.models import LoanFundApplication

from loan_customer.models import LoanApplication


# Create your views here.


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BearerToken])
@permission_classes([IsAuthenticated, IsBankStaff])
def get_bank(request):
    bank = Bank.objects.get(pk=1)
    serializer = BankSerializer(bank)
    return Response(serializer.data, status=status.HTTP_200_OK)


class BaseBankStaffView:  # common permissions across all views
    authentication_classes = [SessionAuthentication, BearerToken]
    permission_classes = [IsAuthenticated, IsBankStaff]


class BankStaffLoanFundApplicationList(BaseBankStaffView, generics.ListAPIView):
    serializer_class = BankStaffLoanFundApplicationSerializer
    queryset = LoanFundApplication.objects.all()


class BankStaffLoanFundApplicationRetrieveUpdate(BaseBankStaffView, generics.RetrieveUpdateAPIView):
    serializer_class = BankStaffLoanFundApplicationSerializer
    queryset = LoanFundApplication.objects.all()

    def partial_update(self, request, *args, **kwargs):  # approve/deny applications. Update bank funds on approve
        kwargs['partial'] = True
        response = services.update_loan_fund_application(kwargs['pk'], request.data.get('status'))
        if response:
            return response
        return self.update(request, *args, **kwargs)

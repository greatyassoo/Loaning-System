from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from authentication.permissions import IsBankStaff
from authentication.models import BearerToken

from .serializers import BankSerializer, BankStaffLoanFundApplicationSerializer, BankStaffLoanApplicationSerializer, \
    LoanListSerializer
from .models import Bank
from . import services

from loan_provider.models import LoanFundApplication

from loan_customer.models import LoanApplication, Loan


# Create your views here.


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BearerToken])
@permission_classes([IsAuthenticated, IsBankStaff])
def get_bank(request):
    bank = Bank.objects.get(pk=1)
    serializer = BankSerializer(bank)
    return Response(serializer.data, status=status.HTTP_200_OK)


class BaseView:  # common permissions across all views
    authentication_classes = [SessionAuthentication, BearerToken]
    permission_classes = [IsAuthenticated, IsBankStaff]


class LoanFundApplicationList(BaseView, generics.ListAPIView):
    serializer_class = BankStaffLoanFundApplicationSerializer
    queryset = LoanFundApplication.objects.all()


class LoanFundApplicationRetrieveUpdate(BaseView, generics.RetrieveUpdateAPIView):
    serializer_class = BankStaffLoanFundApplicationSerializer
    queryset = LoanFundApplication.objects.all()

    def partial_update(self, request, *args, **kwargs):  # approve/deny applications. Update bank funds on approve
        kwargs['partial'] = True
        response = services.update_loan_fund_application(kwargs['pk'], request.data.get('status'))
        if response:
            return response
        return self.update(request, *args, **kwargs)

class LoanApplicationList(BaseView, generics.ListAPIView):
    serializer_class = BankStaffLoanApplicationSerializer
    queryset = LoanApplication.objects.all()


class LoanApplicationRetrieveUpdate(BaseView, generics.RetrieveUpdateAPIView):
    serializer_class = BankStaffLoanApplicationSerializer
    queryset = LoanApplication.objects.all()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        response = services.update_loan_application(kwargs['pk'],
                                                    request.data.get('status'),
                                                    request.data.get('interest_rate'),
                                                    request.data.get('days'))
        if response:
            return response
        return self.update(request, *args, **kwargs)


class LoanList(BaseView, generics.ListAPIView):
    serializer_class = LoanListSerializer
    queryset = Loan.objects.all()


from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from authentication.permissions import IsBankStaff
from authentication.models import BearerToken

from .serializers import BankSerializer, BankLoanFundApplicationSerializer
from .models import Bank

from loan_provider.models import LoanFundApplication


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
    serializer_class = BankLoanFundApplicationSerializer
    queryset = LoanFundApplication.objects.all()


class BankStaffLoanFundApplicationRetrieveUpdate(BaseBankStaffView, generics.RetrieveUpdateAPIView):
    serializer_class = BankLoanFundApplicationSerializer
    queryset = LoanFundApplication.objects.all()

    def partial_update(self, request, *args, **kwargs):  # approve/deny applications. Update bank funds on approve
        kwargs['partial'] = True
        Bank.add_funds(LoanFundApplication.objects.get(id=kwargs['pk']).amount)
        return self.update(request, *args, **kwargs)

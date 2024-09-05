from .models import Bank
from loan_provider.models import LoanFundApplication
from loan_provider.enums import Status

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status as http_status


def update_loan_fund_application(application_id: int, status: str):
    """
    validates if the status provided is correct and adds funds to bank if status=APPROVED
    """
    if status not in Status.values or status == Status.PENDING.value:
        return Response({"detail": f"Invalid status"}, status=http_status.HTTP_400_BAD_REQUEST)

    loan_fund_application = get_object_or_404(LoanFundApplication, pk=application_id)
    if not loan_fund_application.status == Status.PENDING.value:
        return Response({"detail": f"Application already {loan_fund_application.status}"}, status=http_status.HTTP_400_BAD_REQUEST)

    if status == Status.APPROVED.value:
        Bank.add_funds(loan_fund_application.amount)
    return None

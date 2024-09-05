from decimal import Decimal

from .models import Bank
from loan_provider.models import LoanFundApplication
from loan_provider.enums import Status
from loan_customer.models import LoanApplication, Loan

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status as http_status

from datetime import timedelta
from django.utils import timezone

from .serializers import LoanCreateSerializer


def validate_update_application(application_klass, application_id: int, status: str):
    """
    Validates if the status provided is correct and if the application exists.

    Parameters:
        application_klass (class): The class of the application object.
        application_id (int): The ID of the application to be validated.
        status (str): The new status to be validated.

    Returns:
        tuple: A tuple containing a Response object and the application amount.
               If the status is invalid or the application is not in a pending state,
               the Response object will contain an error message and the amount will be None.
               If the validation is successful, the Response object will be None and the amount will be returned.
    """
    if status not in Status.values or status == Status.PENDING.value:
        return (
            Response({"detail": f"Invalid status"}, status=http_status.HTTP_400_BAD_REQUEST), None)
    application = get_object_or_404(application_klass, pk=application_id)
    if not application.status == Status.PENDING.value:
        return (
            Response({"detail": f"Application already {application.status}"}, status=http_status.HTTP_400_BAD_REQUEST), None)
    return None, application


def update_loan_fund_application(loan_fund_application_id: int, status: str):
    """
     adds funds to bank if status=APPROVED
    """
    response, application = validate_update_application(LoanFundApplication, loan_fund_application_id, status)
    if response:  # if error occurs, return response error
        return response

    if status == Status.APPROVED.value:  # else if status is APPROVED add funds
        Bank.add_funds(application.amount)
    return None


def update_loan_application(loan_application_id: int, status: str, interest_rate: Decimal, days: int):
    """
   Updates the status of a loan application and creates a corresponding loan if approved.

   Parameters:
       loan_application_id (int): The ID of the loan application to be updated.
       status (str): The new status to be set for the loan application.
       interest_rate (Decimal): The interest rate for the loan.
       days (int): The duration of the loan in days.

   Returns:
       Response or None: Returns a Response object with an error message if validation fails or
                         if there are insufficient funds. Returns None if the operation is successful.
   """

    response, application = validate_update_application(LoanApplication, loan_application_id, status)
    if response:  # if error occurs, return response error
        return response

    if status == Status.APPROVED.value:
        if Bank.is_sufficient(application.amount):  # only remove funds if bank can cover it
            Bank.remove_funds(application.amount)

            # create loan that corresponds to this loan application
            __create_loan(application, interest_rate, days)
        else:
            return Response({"detail": "Insufficient Funds"}, status=http_status.HTTP_400_BAD_REQUEST)
    return None


def __create_loan(loan_application: LoanApplication, interest_rate: Decimal, days: int):
    start_date = timezone.now().date()
    end_date = start_date + timedelta(days=days)

    serializer = LoanCreateSerializer(data={"interest_rate": interest_rate, "end_date": end_date})
    if serializer.is_valid(raise_exception=True):
        loan = Loan(
            amount=loan_application.amount,
            interest_rate=interest_rate,
            start_date=start_date,
            end_date=end_date,
            customer=loan_application.customer
        )
        loan.save()

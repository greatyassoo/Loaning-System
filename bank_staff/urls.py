from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_bank),
    path("loan-fund-application/", views.BankStaffLoanFundApplicationList.as_view()),
    path("loan-fund-application/<int:pk>/", views.BankStaffLoanFundApplicationRetrieveUpdate.as_view()),
]
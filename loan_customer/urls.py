from django.urls import path
from . import views

urlpatterns = [
    path("loan-application", views.LoanApplicationListCreate.as_view()),
    path("loan", views.LoanList.as_view()),
    path("payment", views.PaymentListCreate.as_view()),
]

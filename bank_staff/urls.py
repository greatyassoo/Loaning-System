from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_bank),
    path("loan-fund-application/", views.LoanFundApplicationList.as_view()),
    path("loan-fund-application/<int:pk>/", views.LoanFundApplicationRetrieveUpdate.as_view()),
    path("loan-application/", views.LoanApplicationList.as_view()),
    path("loan-application/<int:pk>/", views.LoanApplicationRetrieveUpdate.as_view()),

]
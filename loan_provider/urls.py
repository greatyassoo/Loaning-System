from django.urls import path
from .views import LoanFundApplicationListCreate


urlpatterns = [
    path("", LoanFundApplicationListCreate.as_view())
]
from rest_framework import generics

from .models import LoanFundApplication
from .serializers import LoanFundApplicationSerializer

# Create your views here.


class LoanFundApplicationListCreate(generics.ListCreateAPIView):
    queryset = LoanFundApplication.objects.all()
    serializer_class = LoanFundApplicationSerializer

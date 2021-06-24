from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AccountTypeSerializer
from .models import AccountType

# Create your views here.

class AccountTypeViewset(viewsets.ModelViewSet):
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer
from rest_framework import serializers
from .models import AccountType


class AccountTypeSerializer(serializers.Serializer):
    class Meta:
        model = AccountType
        fields = '__all__'
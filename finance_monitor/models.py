from django.db import models
from django.db.models.base import Model

# Create your models here.


class AccountType(models.Model):
    type_name = models.CharField(max_length=20)

class Account(models.Model):
    type = models.ForeignKey(AccountType, on_delete=models.PROTECT)
    account_name = models.CharField(max_length=20)

class FinanceBalance(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    balance = models.IntegerField()
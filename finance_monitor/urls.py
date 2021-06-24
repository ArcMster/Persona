from django.contrib import admin
from django.urls import path,include
from .import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('account-type',views.AccountTypeViewset)

urlpatterns = [
    path('api/',include(router.urls))
]
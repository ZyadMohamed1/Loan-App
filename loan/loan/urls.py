"""
URL configuration for loan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers

from applicationRequests.views import (
    BorrowerView,
    InvestorView,
    LoanRequestView,
    LoanOfferView,
    LoanFundingView,
    PaymentView,
)

router = routers.DefaultRouter()
router.register(r'borrowers', BorrowerView)
router.register(r'investors', InvestorView)
router.register(r'loan-requests', LoanRequestView)
router.register(r'loan-offers', LoanOfferView)
router.register(r'loan-funding', LoanFundingView, basename='loan-funding')
router.register(r'payments', PaymentView)

urlpatterns = [
    path('', include(router.urls)),
]



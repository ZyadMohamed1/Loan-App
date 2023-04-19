from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Borrower, Investor, LoanRequest, LoanOffer, Loan, Payment
from .serializers import BorrowerSerializer, InvestorSerializer, LoanRequestSerializer, LoanOfferSerializer, LoanSerializer, PaymentSerializer

import datetime

class BorrowerView(viewsets.ModelViewSet):
    serializer_class = BorrowerSerializer
    queryset = Borrower.objects.all()

class BorrowerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

class InvestorView(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

class InvestorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

class LoanRequestView(viewsets.ModelViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer

class LoanRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer

class LoanOfferView(viewsets.ModelViewSet):
    queryset = LoanOffer.objects.all()
    serializer_class = LoanOfferSerializer

class LoanOfferDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoanOffer.objects.all()
    serializer_class = LoanOfferSerializer

class LoanFundingView(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):

        loan_request_id = request.data.get('loan_request_id')
        investor_id = request.data.get('investor_id')
        loan_request = LoanRequest.objects.get(id=loan_request_id)
        investor = Investor.objects.get(id=investor_id)
        total_loan_amount = loan_request.loan_amount + 3  # add lenme fee
        if investor.balance < total_loan_amount:
            return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
        investor.balance -= total_loan_amount
        investor.save()
        payment_per_month = total_loan_amount / loan_request.loan_period
        today = datetime.date.today()
        loan_list = []
        for i in range(1, loan_request.loan_period + 1):
            next_month = today + datetime.timedelta(days=30 * i)
            next_month_str = next_month.strftime('%Y-%m-%d')
            loan = Loan.objects.create(
                borrower=loan_request.borrower,
                investor=investor,
                loan_request=loan_request,
                total_loan_amount=total_loan_amount,
                lenme_fee=3,
                status='Funded',
                payment_per_month=payment_per_month,
                date=next_month_str
            )
            loan_list.append(LoanSerializer(loan).data)
        return Response(loan_list)

class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        print(payment)
        loan = payment.loan
        print(loan.status)
        today_date = datetime.date.today()
        if loan.date >= today_date:
            if payment.payment_amount == loan.payment_per_month:
                loan.status = 'Completed'
        
        loan.save()
        

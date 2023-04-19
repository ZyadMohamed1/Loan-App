from django.db import models
import datetime

class Borrower(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

class Investor(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class LoanRequest(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_period = models.IntegerField(help_text='Loan period in months')
    
    def __str__(self):
        return f'{self.borrower.name} - ${self.loan_amount}'

class LoanOffer(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    loan_request = models.ForeignKey(LoanRequest, on_delete=models.CASCADE)
    annual_interest_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text='Annual interest rate as a percentage')
    
    def __str__(self):
        return f'{self.investor.name} - {self.loan_request} - {self.annual_interest_rate}%'

class Loan(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    loan_request = models.ForeignKey(LoanRequest, on_delete=models.CASCADE)
    total_loan_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Total loan amount including Lenme fee')
    lenme_fee = models.DecimalField(max_digits=5, decimal_places=2, default=3.00, help_text='Lenme fee')
    status = models.CharField(max_length=255, choices=[('Funded', 'Funded'), ('Completed', 'Completed')], default='Funded')
    payment_per_month = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,help_text='payment per month')
    date = models.DateField(default=datetime.date(2022, 4, 20))

    def __str__(self):
        return f'{self.borrower.name} - {self.investor.name} - ${self.total_loan_amount}'

class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(default=datetime.date(2022, 4, 20))
    
    def __str__(self):
        return f'{self.loan} - ${self.payment_amount} - {self.payment_date}'
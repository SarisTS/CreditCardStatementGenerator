from django.test import TestCase
from rest_framework.test import APIClient
from .models import Customer, CreditCardAccount, Transaction, RewardPoint
from datetime import date

class StatementGenerationTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create sample customer
        self.customer = Customer.objects.create(
            CustomerID=1001,
            FirstName='Saris',
            LastName='TS',
            DateOfBirth='1995-01-01',
            Address='123 Sample St',
            City='KL',
            State='Selangor',
            PostalCode='50000',
            Country='Malaysia',
            PhoneNumber='0123456789',
            Email='saris@example.com',
            IdentificationNumber='IC12345678',
            RegistrationDate='2020-01-01',
            Status='active'
        )

        # Create account
        self.account = CreditCardAccount.objects.create(
            Customer=self.customer,
            CardNumber='4024007123456788',
            CardType='Visa',
            CreditLimit=5000.00,
            CurrentBalance=1200.00,
            AvailableCredit=3800.00,
            ExpiryDate='2026-12-31',
            IssueDate='2021-01-01',
            PaymentDueDate='2024-04-30',
            MinimumPaymentPercentage='5%',
            InterestRate='15%',
            Status='active',
            PreviousBalance=1000.00,
            TotalPayment=800.00,
            NewPurchases=400.00,
            MinDue=60.00,
            TotalDue=600.00,
            CashLimit=2000.00,
            AvailableCash=1800.00
        )

        # Create a transaction
        Transaction.objects.create(
            Account=self.account,
            TransactionDate='2024-04-01',
            MerchantName='Shopee',
            MerchantLocation='KL',
            MerchantCategory='E-commerce',
            Amount=200.00,
            TransactionType='Purchase'
        )

        # Create reward points
        RewardPoint.objects.create(
            Account=self.account,
            PointsEarned=100,
            PointsRedeemed=20
        )

    def test_generate_statement_success(self):
        response = self.client.get('/api/generate-statement/?customer_id=1001&language=en')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['success'])
        self.assertIn('pdf_url', response.data)

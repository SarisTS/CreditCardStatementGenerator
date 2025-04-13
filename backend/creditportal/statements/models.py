from django.db import models
from django.utils.translation import gettext_lazy as _

# Reusable status choices
STATUS_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('pending', 'Pending'),
    ('blocked', 'Blocked'),
]

class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    Address = models.TextField()
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    PostalCode = models.CharField(max_length=10)
    Country = models.CharField(max_length=20)
    PhoneNumber = models.CharField(max_length=15)
    Email = models.EmailField(max_length=254)
    IdentificationNumber = models.CharField(max_length=50)
    RegistrationDate = models.DateField()
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class CreditCardAccount(models.Model):
    AccountID = models.AutoField(primary_key=True)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    CardNumber = models.CharField(max_length=20)
    CardType = models.CharField(max_length=20)
    CreditLimit = models.DecimalField(max_digits=10, decimal_places=2)
    CurrentBalance = models.DecimalField(max_digits=10, decimal_places=2)
    AvailableCredit = models.DecimalField(max_digits=10, decimal_places=2)
    ExpiryDate = models.DateField()
    IssueDate = models.DateField()
    PaymentDueDate = models.DateField()
    MinimumPaymentPercentage = models.CharField(max_length=50)
    InterestRate = models.CharField(max_length=50)
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    # Additional fields you added
    PreviousBalance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    TotalPayment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    NewPurchases = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    MinDue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    TotalDue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    CashLimit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    AvailableCash = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.CardNumber

class Transaction(models.Model):
    TransactionID = models.AutoField(primary_key=True)
    Account = models.ForeignKey(CreditCardAccount, on_delete=models.CASCADE)
    TransactionDate = models.DateField()
    MerchantName = models.CharField(max_length=100)
    MerchantLocation = models.CharField(max_length=100)
    MerchantCategory = models.CharField(max_length=100)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    TransactionType = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.TransactionDate} - {self.MerchantName}"

class RewardPoint(models.Model):
    RewardID = models.AutoField(primary_key=True)
    Account = models.ForeignKey(CreditCardAccount, on_delete=models.CASCADE)
    PointsEarned = models.IntegerField(default=0)
    PointsRedeemed = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.Account.CardNumber} - Points"

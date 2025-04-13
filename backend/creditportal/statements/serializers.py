from rest_framework import serializers
from .models import Customer, CreditCardAccount, Transaction, RewardPoint

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CreditCardAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCardAccount
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class RewardPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardPoint
        fields = '__all__'

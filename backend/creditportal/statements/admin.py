from django.contrib import admin
from .models import Customer, CreditCardAccount, Transaction, RewardPoint

admin.site.register(Customer)
admin.site.register(CreditCardAccount)
admin.site.register(Transaction)
admin.site.register(RewardPoint)

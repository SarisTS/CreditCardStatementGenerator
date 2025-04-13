from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import generate_pdf
from .models import Customer, CreditCardAccount, Transaction, RewardPoint
from django.db.models import Sum

@api_view(['GET'])
def generate_statement(request):
    customer_id = request.GET.get("customer_id")
    language = request.GET.get("language")

    if not customer_id:
        return Response({'success': False, 'error': 'Customer ID is required'})

    try:
        # Fetch customer
        customer = Customer.objects.filter(CustomerID=customer_id).first()
        if not customer:
            return Response({'success': False, 'error': 'Customer not found'})

        # Fetch account
        account = CreditCardAccount.objects.filter(Customer=customer).first()
        if not account:
            return Response({'success': False, 'error': 'Account not found'})

        # Fetch recent 10 transactions
        transactions = list(
            Transaction.objects.filter(Account=account)
            .order_by('-TransactionDate')[:10]
            .values()
        )

        # Calculate reward points
        reward_agg = RewardPoint.objects.filter(Account=account).aggregate(
            AvailablePoints=Sum('PointsEarned') - Sum('PointsRedeemed')
        )
        rewards = {
            'AvailablePoints': reward_agg['AvailablePoints'] or 0
        }

        # Format customer data for PDF
        customer_data = {
            'FirstName': customer.FirstName,
            'LastName': customer.LastName,
        }

        # Format account data for PDF
        account_data = {
            'CardNumber': account.CardNumber,
            'CardType': account.CardType,
            'CurrentBalance': account.CurrentBalance,
            'PreviousBalance': getattr(account, 'PreviousBalance', 0.00),
            'TotalPayment': getattr(account, 'TotalPayment', 0.00),
            'NewPurchases': getattr(account, 'NewPurchases', 0.00),
            'Interest': getattr(account, 'InterestRate', 0.00),
            'MinDue': getattr(account, 'MinDue', 0.00),
            'TotalDue': getattr(account, 'TotalDue', 0.00),
            'DueDate': account.PaymentDueDate,
            'CreditLimit': account.CreditLimit,
            'AvailableCredit': account.AvailableCredit,
            'CashLimit': account.CashLimit,
            'AvailableCash': account.AvailableCash,
        }

        # Generate PDF
        filename = generate_pdf(customer_data, account_data, transactions, rewards, language)

        return Response({'success': True, 'pdf_url': f'/media/{filename}'})

    except Exception as e:
        return Response({'success': False, 'error': str(e)})

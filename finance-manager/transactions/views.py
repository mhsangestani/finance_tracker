from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.db.models import Sum, Case, When, IntegerField


def dashboard(request):
    transactions = Transaction.objects.order_by('-date')[:20]

    # جمع‌های خلاصه
    totals = Transaction.objects.aggregate(
        total_income = Sum(
            Case(When(type=Transaction.INCOME,  then='amount'),
                 default=0, output_field=IntegerField())),
        total_expense = Sum(
            Case(When(type=Transaction.EXPENSE, then='amount'),
                 default=0, output_field=IntegerField()))
    )
    balance = (totals['total_income'] or 0) - (totals['total_expense'] or 0)

    context = {
        'transactions':  transactions,
        'total_income':  totals['total_income'] or 0,
        'total_expense': totals['total_expense'] or 0,
        'balance':       balance,
        'form':          TransactionForm(),
    }
    return render(request, 'index.html', context)

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
    else:
        form = TransactionForm()

    return redirect('dashboard')
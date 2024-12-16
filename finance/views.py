from django.shortcuts import render, redirect
from .models import Budget, Income, Expense
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):
    budgets = request.user.budgets.all()
    return render(request, 'finance/dashboard.html', {'budgets': budgets})

@login_required
def add_budget(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            Budget.objects.create(name=name, user=request.user)
            return redirect('dashboard')  # Redirect to the dashboard after creating a budget
    return render(request, 'finance/add_budget.html')

@login_required
def budget_detail(request, budget_id):
    budget = Budget.objects.get(id=budget_id, user=request.user)
    incomes = budget.incomes.all()
    expenses = budget.expenses.all()

    total_income = sum(income.amount for income in incomes)
    total_expense = sum(expense.amount for expense in expenses)
    balance = total_income - total_expense

    return render(request, 'finance/budget_detail.html', {
        'budget': budget,
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    })

@login_required
def add_income(request, budget_id):
    if request.method == 'POST':
        budget = Budget.objects.get(id=budget_id, user=request.user)
        description = request.POST['description']
        amount = request.POST['amount']
        Income.objects.create(budget=budget, description=description, amount=amount)
        return redirect('budget_detail', budget_id=budget_id)
    return render(request, 'finance/add_income.html')

@login_required
def add_expense(request, budget_id):
    if request.method == 'POST':
        budget = Budget.objects.get(id=budget_id, user=request.user)
        description = request.POST['description']
        amount = request.POST['amount']
        Expense.objects.create(budget=budget, description=description, amount=amount)
        return redirect('budget_detail', budget_id=budget_id)
    return render(request, 'finance/add_expense.html')
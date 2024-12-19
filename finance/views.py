from django.shortcuts import render, redirect
from .models import Budget, Income, Expense
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

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
    budget = Budget.objects.get(id=budget_id, user=request.user)
    if request.method == 'POST':
        description = request.POST['description']
        amount = request.POST['amount']
        Income.objects.create(budget=budget, description=description, amount=amount)
        return redirect('budget_detail', budget_id=budget_id)
    return render(request, 'finance/add_income.html', {'budget': budget})

@login_required
def add_expense(request, budget_id):
    budget = Budget.objects.get(id=budget_id, user=request.user)
    if request.method == 'POST':
        description = request.POST['description']
        amount = request.POST['amount']
        Expense.objects.create(budget=budget, description=description, amount=amount)
        return redirect('budget_detail', budget_id=budget_id)
    return render(request, 'finance/add_expense.html', {'budget': budget})

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect to login page after logout

@login_required
def delete_budgets(request):
    if request.method == "POST":
        budget_ids = request.POST.getlist('budgets')  # Get a list of budget IDs
        if budget_ids:
            # Delete only budgets that belong to the logged-in user
            Budget.objects.filter(id__in=budget_ids, user=request.user).delete()
            messages.success(request, "Selected budgets have been deleted.")
        else:
            messages.error(request, "No budgets were selected.")
        return redirect('dashboard')
    return JsonResponse({"error": "Invalid request method."}, status=400)

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after sign-up
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
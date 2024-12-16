from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('budget/<int:budget_id>/', views.budget_detail, name='budget_detail'),
    path('budget/<int:budget_id>/add-income/', views.add_income, name='add_income'),
    path('budget/<int:budget_id>/add-expense/', views.add_expense, name='add_expense'),
    path('add-budget/', views.add_budget, name='add_budget'),  # New URL for adding a budget
]
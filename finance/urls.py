from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('delete_budgets/', views.delete_budgets, name='delete_budgets'),
    path('budget/<int:budget_id>/', views.budget_detail, name='budget_detail'),
    path('budget/<int:budget_id>/add-income/', views.add_income, name='add_income'),
    path('budget/<int:budget_id>/add-expense/', views.add_expense, name='add_expense'),
    path('add-budget/', views.add_budget, name='add_budget'),
]
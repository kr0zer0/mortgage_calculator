from imp import new_module
from django.urls import path
from .views import *
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('banks/', BankListView.as_view(), name='bank_list'),
    path('banks/new/', BankCreateView.as_view(), name='add_bank'),
    path('banks/<int:pk>/edit/', BankUpdateView.as_view(), name='edit_bank'),
    path('banks/<int:pk>/delete/', BankDeleteView.as_view(), name='delete_bank'),
    path('calculator/', CalculatorFormView.as_view(), name='calculator'),
    path('result/', result , name='result')
]
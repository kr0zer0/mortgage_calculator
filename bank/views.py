import imp
from itertools import tee
from re import template
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, FormView
from .models import Bank
from .forms import CalculatorForm

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class BankCreateView(CreateView):
    model = Bank
    template_name = 'new_bank.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('bank_list')


class BankListView(ListView):
    model = Bank
    template_name = 'bank_list.html'


class BankUpdateView(UpdateView):
    model = Bank
    template_name = 'edit_bank.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('bank_list')


class BankDeleteView(DeleteView):
    model = Bank
    template_name = 'delete_bank.html'

    def get_success_url(self):
        return reverse('bank_list')


class CalculatorFormView(FormView):
    template_name = 'calculator.html'
    form_class = CalculatorForm

    def form_valid(self, form):
        bank = self.request.POST['bank']
        self.request.session['bank'] = bank
        self.request.session['loan'] = self.request.POST['initial_lone']
        return redirect('result')


def result(request):
    bank_id = request.session.get('bank')
    bank = Bank.objects.get(pk=bank_id)

    loan = int(request.session.get('loan'))
    annual_int = bank.interest_rate/100
    month_num = bank.loan_term*12
    
    monthly_pay = (loan*(annual_int/12)*((1+annual_int/12)**month_num))/((1+annual_int/12)**month_num-1)
    monthly_pay = int(monthly_pay)
    return render(request, 'result.html', {'result': monthly_pay})

from django import forms
from .models import Bank


class CalculatorForm(forms.Form):
    initial_lone = forms.IntegerField()
    down_payment = forms.IntegerField()
    bank = forms.ModelChoiceField(Bank.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        initial_lone = cleaned_data.get("initial_lone")
        down_payment = cleaned_data.get("down_payment")
        bank = cleaned_data.get("bank")
        bank_minimum_down_payment = (initial_lone/100) * bank.minimum_down_payment

        if bank_minimum_down_payment > down_payment:
            msg = f"The minimum down payment for your initial loan at this bank is {bank_minimum_down_payment}"
            self.add_error("down_payment", msg)

        if initial_lone > bank.maximum_loan:
            msg = f"The maximum loan at this bank is {bank.maximum_loan}"
            self.add_error("initial_lone", msg)
from django import forms


class DepositForm(forms.Form):
    amount = forms.IntegerField(min_value=1, label="Amount")

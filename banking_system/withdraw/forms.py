from django import forms


class WithdrawForm(forms.Form):
    amount = forms.IntegerField(min_value=1, label="Amount")

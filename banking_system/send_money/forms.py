from django import forms


class SendMoneyForm(forms.Form):
    to = forms.CharField(max_length=50)
    amount = forms.IntegerField(min_value=1, label="Amount")

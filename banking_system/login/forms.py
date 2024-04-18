from django import forms


class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=50, label="User Name")

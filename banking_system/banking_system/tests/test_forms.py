from django.test import SimpleTestCase

from login.forms import LoginForm
from deposit.forms import DepositForm
from withdraw.forms import WithdrawForm
from send_money.forms import SendMoneyForm


class TestForms(SimpleTestCase):
    def test_empty(self):
        form_classes = [LoginForm, DepositForm, WithdrawForm, SendMoneyForm]
        for form_class in form_classes:
            form = form_class()
            self.assertFalse(form.is_valid())

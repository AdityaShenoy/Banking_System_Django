from django.test import SimpleTestCase

from ..forms import WithdrawForm


class TestWithdrawForms(SimpleTestCase):
    def test_negative(self):
        form = WithdrawForm({"amount": -1})
        self.assertFalse(form.is_valid())

    def test_zero(self):
        form = WithdrawForm({"amount": -0})
        self.assertFalse(form.is_valid())

    def test_correct(self):
        form = WithdrawForm({"amount": 1})
        self.assertTrue(form.is_valid())

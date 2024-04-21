from django.test import SimpleTestCase

from ..forms import DepositForm


class TestDepositForms(SimpleTestCase):
    def test_empty(self):
        form = DepositForm()
        self.assertFalse(form.is_valid())

    def test_negative(self):
        form = DepositForm({"amount": -1})
        self.assertFalse(form.is_valid())

    def test_zero(self):
        form = DepositForm({"amount": -0})
        self.assertFalse(form.is_valid())

    def test_correct(self):
        form = DepositForm({"amount": 1})
        self.assertTrue(form.is_valid())

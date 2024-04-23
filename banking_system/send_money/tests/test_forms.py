from django.test import SimpleTestCase

from ..forms import SendMoneyForm


class TestSendMoneyForms(SimpleTestCase):

    def test_empty(self):
        form = SendMoneyForm()
        self.assertFalse(form.is_valid())

    def test_empty_to(self):
        form = SendMoneyForm({"to": "", "amount": 1})
        self.assertFalse(form.is_valid())

    def test_empty_big_to(self):
        form = SendMoneyForm({"to": "a" * 51, "amount": 1})
        self.assertFalse(form.is_valid())

    def test_negative(self):
        form = SendMoneyForm({"to": "User 1", "amount": -1})
        self.assertFalse(form.is_valid())

    def test_zero(self):
        form = SendMoneyForm({"to": "User 1", "amount": 0})
        self.assertFalse(form.is_valid())

    def test_correct(self):
        form = SendMoneyForm({"to": "User 1", "amount": 1})
        self.assertTrue(form.is_valid())

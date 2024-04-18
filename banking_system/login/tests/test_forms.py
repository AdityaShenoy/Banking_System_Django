from django.test import SimpleTestCase

from ..forms import LoginForm


class TestLoginForms(SimpleTestCase):
    def test_empty(self):
        form = LoginForm()
        self.assertFalse(form.is_valid())

    def test_big_name(self):
        form = LoginForm({"user_name": "a" * 51})
        self.assertFalse(form.is_valid())

    def test_correct(self):
        form = LoginForm({"user_name": "User 1"})
        self.assertTrue(form.is_valid())

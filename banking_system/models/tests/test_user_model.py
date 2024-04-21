from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from ..user_model import UserModel
from ..account_model import AccountModel


class TestLoginForms(TestCase):
    def test_empty(self):
        with self.assertRaises(ValidationError):
            UserModel.objects.create(name="")

    def test_big_name(self):
        with self.assertRaises(ValidationError):
            UserModel.objects.create(name="a" * 51)

    def test_duplicate_name(self):
        UserModel.objects.create(name="a")
        with self.assertRaises(IntegrityError):
            UserModel.objects.create(name="a")

    def test_create(self):
        UserModel.create("User 1")
        self.assertEquals(UserModel.objects.get(name="User 1").name, "User 1")
        self.assertEquals(
            AccountModel.objects.get(user__name="User 1").user.name, "User 1"
        )
        self.assertEquals(AccountModel.objects.get(user__name="User 1").balance, 0)

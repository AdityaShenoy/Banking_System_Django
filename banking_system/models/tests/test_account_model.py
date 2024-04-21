from django.test import TestCase
from django.core.exceptions import ValidationError

from ..user_model import UserModel
from ..account_model import AccountModel


class TestAccountModel(TestCase):
    def test_cascade_delete(self):
        UserModel.create(name="User 1")
        UserModel.objects.get(name="User 1").delete()
        self.assertEquals(len(AccountModel.objects.filter(user__name="User 1")), 0)

    def test_negative_balance(self):
        UserModel.create(name="User 1")
        account = AccountModel.objects.get(user__name="User 1")
        account.balance = -1
        with self.assertRaises(ValidationError):
            account.save()  # type: ignore

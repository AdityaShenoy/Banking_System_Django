from django.test import TestCase, Client
from django.urls import reverse

from models.transaction_model import TransactionModel
from models.account_model import AccountModel


class TestDepositViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post(reverse("login"), {"user_name": "User 1"})

    def test_get(self):
        response = self.client.get(reverse("deposit"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "deposit.html")

    def test_post_without_login(self):
        client = Client()
        response = client.post(reverse("deposit"), {"amount": 1})
        self.assertEquals(response.status_code, 302)

    def test_post_invalid(self):
        response = self.client.post(reverse("deposit"), {})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "deposit.html")

    def test_post_valid(self):
        response = self.client.post(reverse("deposit"), {"amount": 1})
        self.assertEquals(response.status_code, 302)
        transaction = TransactionModel.objects.filter(receiver__name="User 1")[0]
        account = AccountModel.objects.get(user__name="User 1")
        self.assertIsNone(transaction.sender)
        self.assertIsNotNone(transaction.receiver)
        if transaction.receiver is not None:  # Adding this check for type checking
            self.assertEquals(transaction.receiver.name, "User 1")
        self.assertEquals(transaction.amount, 1)
        self.assertEquals(account.balance, 1)

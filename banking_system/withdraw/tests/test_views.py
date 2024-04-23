from django.test import TestCase, Client
from django.urls import reverse

from models.transaction_model import TransactionModel
from models.account_model import AccountModel


class TestWithdrawViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post(reverse("login"), {"user_name": "User 1"})
        self.client.post(reverse("deposit"), {"amount": 100})

    def test_get(self):
        response = self.client.get(reverse("withdraw"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "withdraw.html")

    def test_get_without_login(self):
        client = Client()
        response = client.get(reverse("withdraw"))
        self.assertEquals(response.status_code, 302)

    def test_post_without_login(self):
        client = Client()
        response = client.post(reverse("withdraw"), {"amount": 1})
        self.assertEquals(response.status_code, 302)

    def test_post_invalid(self):
        response = self.client.post(reverse("withdraw"), {})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "withdraw.html")

    def test_post_valid(self):
        response = self.client.post(reverse("withdraw"), {"amount": 1})
        self.assertEquals(response.status_code, 302)
        transaction = TransactionModel.objects.filter(sender__name="User 1")[0]
        account = AccountModel.objects.get(user__name="User 1")
        self.assertIsNone(transaction.receiver)
        self.assertIsNotNone(transaction.sender)
        if transaction.sender is not None:  # Adding this check for type checking
            self.assertEquals(transaction.sender.name, "User 1")
        self.assertEquals(transaction.amount, 1)
        self.assertEquals(account.balance, 99)

    def test_post_higher_amount_than_balance(self):
        response = self.client.post(reverse("withdraw"), {"amount": 101})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed("withdraw.html")
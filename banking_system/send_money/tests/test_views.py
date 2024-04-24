from django.test import TestCase, Client
from django.urls import reverse

from models.transaction_model import TransactionModel
from models.account_model import AccountModel


class TestSendMoneyViews(TestCase):
    def setUp(self):
        self.client1 = Client()
        self.client1.post(reverse("login"), {"user_name": "User 1"})
        self.client1.post(reverse("deposit"), {"amount": 100})

        self.client2 = Client()
        self.client2.post(reverse("login"), {"user_name": "User 2"})

    def test_post_valid(self):
        response = self.client1.post(
            reverse("send_money"), {"to": "User 2", "amount": 1}
        )
        self.assertEquals(response.status_code, 302)
        transaction = TransactionModel.objects.get(sender__name="User 1")
        account1 = AccountModel.objects.get(user__name="User 1")
        account2 = AccountModel.objects.get(user__name="User 2")

        self.assertIsNotNone(transaction.sender)
        if transaction.sender is not None:  # Adding this check for type checking
            self.assertEquals(transaction.sender.name, "User 1")
        self.assertIsNotNone(transaction.receiver)
        if transaction.receiver is not None:  # Adding this check for type checking
            self.assertEquals(transaction.receiver.name, "User 2")
        self.assertEquals(transaction.amount, 1)
        self.assertEquals(account1.balance, 99)
        self.assertEquals(account2.balance, 1)

    def test_post_higher_amount_than_balance(self):
        response = self.client1.post(
            reverse("send_money"), {"to": "User 2", "amount": 101}
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed("send_money.html")

from django.test import TestCase
from django.core.exceptions import ValidationError

from ..user_model import UserModel
from ..transaction_model import TransactionModel


class TestTransactionModel(TestCase):
    def setUp(self):
        self.sender = UserModel.create("Sender")
        self.receiver = UserModel.create("Receiver")

    def test_create(self):
        TransactionModel.objects.create(
            sender=self.sender, receiver=self.receiver, amount=1
        )
        transaction = TransactionModel.objects.get(sender__name="Sender")
        self.assertEquals(transaction.sender.name, "Sender")
        self.assertEquals(transaction.receiver.name, "Receiver")
        self.assertEquals(transaction.amount, 1)
        self.assertIsNotNone(transaction.time)

    def test_negative_amount(self):
        with self.assertRaises(ValidationError):
            TransactionModel.objects.create(
                sender=self.sender, receiver=self.receiver, amount=-1
            )

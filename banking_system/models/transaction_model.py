from django.db import models
from django.core.exceptions import ValidationError


from .user_model import UserModel


# Create your models here.
class TransactionModel(models.Model):
    sender = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="sent_transactions",
        null=True,  # for deposit transactions
    )
    receiver = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="received_transactions",
        null=True,  # For withdraw transactions
    )
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now=True)

    def check_negative_amount(self):
        if self.amount <= 0:
            raise ValidationError("Transaction amount must be positive")

    def save(self, *args, **kwargs):  # type: ignore
        self.check_negative_amount()
        super().save(*args, **kwargs)  # type: ignore

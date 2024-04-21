from django.db import models
from django.core.exceptions import ValidationError

from .user_model import UserModel


# Create your models here.
class AccountModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    balance = models.IntegerField()

    def save(self, *args, **kwargs):  # type: ignore
        self.check_negative_balance()
        super().save(*args, **kwargs)  # type: ignore

    def check_negative_balance(self):
        if self.balance < 0:
            raise ValidationError("Balance cannot be negative")

    def __str__(self):
        return self.user.name

from django.db import models
from .user_model import UserModel


# Create your models here.
class AccountModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    balance = models.IntegerField()

    def __str__(self):
        return self.user.name

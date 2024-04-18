from django.db import models


# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)

    def __str__(self):
        return self.name

    @staticmethod
    def create(name: str):
        # Adding import here to avoid circular import
        from .account_model import AccountModel

        user = UserModel.objects.create(name=name)
        AccountModel.objects.create(user=user, balance=0)

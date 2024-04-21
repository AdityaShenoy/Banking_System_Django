from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # type: ignore
        self.check_empty_name()
        self.check_big_name()
        return super().save(*args, **kwargs)  # type: ignore

    def check_empty_name(self):
        if self.name == "":
            raise ValidationError("Name must not be empty")

    def check_big_name(self):
        if len(self.name) > 50:
            raise ValidationError("Name must not exceed 50 characters")

    @staticmethod
    def create(name: str):
        # Adding import here to avoid circular import
        from .account_model import AccountModel

        user = UserModel.objects.create(name=name)
        AccountModel.objects.create(user=user, balance=0)
        return user

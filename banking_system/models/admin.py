from django.contrib import admin

from .account_model import AccountModel
from .user_model import UserModel
from .transaction_model import TransactionModel

# Register your models here.
admin.site.register(AccountModel)
admin.site.register(UserModel)
admin.site.register(TransactionModel)

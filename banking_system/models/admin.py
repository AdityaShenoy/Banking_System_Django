from django.contrib import admin

from .account_model import AccountModel
from .user_model import UserModel

# Register your models here.
admin.site.register(AccountModel)
admin.site.register(UserModel)

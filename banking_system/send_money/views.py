from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views import View
from django.urls import reverse

from .forms import SendMoneyForm
from models.transaction_model import TransactionModel
from models.user_model import UserModel
from models.account_model import AccountModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.http.request import HttpRequest


# Create your views here.
class SendMoneyView(View):
    def render_helper(self, request: "HttpRequest", form: SendMoneyForm):
        context = {"form": form}
        return render(request, "send_money.html", context)

    def get(self, request: "HttpRequest"):
        if not request.session.get("user_name"):
            return HttpResponseRedirect(reverse("login"))
        return self.render_helper(request, SendMoneyForm())

    def post(self, request: "HttpRequest"):
        user_name = request.session.get("user_name")
        if not user_name:
            return HttpResponseRedirect(reverse("login"))

        form = SendMoneyForm(request.POST)
        if not form.is_valid():
            return self.render_helper(request, form)

        if self.amount_gt_balance(user_name, form):
            form.add_error("amount", "Amount cannot exceed the account balance")
            return self.render_helper(request, form)

        self.handle_valid_transaction(user_name, form)
        return HttpResponseRedirect(reverse("dashboard"))

    def amount_gt_balance(self, user_name: str, form: SendMoneyForm):
        account = AccountModel.objects.get(user__name=user_name)
        amount = form.cleaned_data.get("amount")
        return amount is not None and amount > account.balance

    def handle_valid_transaction(self, user_name: str, form: SendMoneyForm):
        sender = UserModel.objects.get(name=user_name)
        receiver_name = form.cleaned_data.get("to")
        receiver = UserModel.objects.get(name=receiver_name)
        amount = form.cleaned_data.get("amount")
        TransactionModel.objects.create(sender=sender, receiver=receiver, amount=amount)
        sender_account = AccountModel.objects.get(user__name=user_name)
        receiver_account = AccountModel.objects.get(user__name=receiver_name)

        sender_account.balance -= amount  # type: ignore
        receiver_account.balance += amount  # type: ignore
        sender_account.save()  # type: ignore
        receiver_account.save()  # type: ignore

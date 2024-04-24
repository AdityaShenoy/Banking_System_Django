from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.views import View
from django.urls import reverse

from .forms import WithdrawForm
from models.transaction_model import TransactionModel
from models.user_model import UserModel
from models.account_model import AccountModel
from banking_system.utils.render_form import render_form


# Create your views here.
class WithdrawView(View):
    def render_helper(self, request: HttpRequest, form: WithdrawForm):
        return render_form(request, "Withdraw", "withdraw", form)

    def get(self, request: HttpRequest):
        if not request.session.get("user_name"):
            return HttpResponseRedirect(reverse("login"))
        return self.render_helper(request, WithdrawForm())

    def post(self, request: HttpRequest):
        user_name = request.session.get("user_name")
        if not user_name:
            return HttpResponseRedirect(reverse("login"))

        form = WithdrawForm(request.POST)
        if not form.is_valid():
            return self.render_helper(request, form)
        if self.amount_gt_balance(user_name, form):
            form.add_error(
                "amount", "Withdraw amount cannot exceed the account balance"
            )
            return self.render_helper(request, form)
        self.handle_valid_withdraw(user_name, form)
        return HttpResponseRedirect(reverse("dashboard"))

    def amount_gt_balance(self, user_name: str, form: WithdrawForm):
        account = AccountModel.objects.get(user__name=user_name)
        amount = form.cleaned_data.get("amount")
        return amount is not None and amount > account.balance

    def handle_valid_withdraw(self, user_name: str, form: WithdrawForm):
        sender = UserModel.objects.get(name=user_name)
        amount = form.cleaned_data.get("amount")
        TransactionModel.objects.create(sender=sender, receiver=None, amount=amount)
        account = AccountModel.objects.get(user__name=user_name)

        account.balance -= amount  # type: ignore
        account.save()  # type: ignore

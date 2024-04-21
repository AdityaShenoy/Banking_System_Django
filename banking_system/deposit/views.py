from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views import View
from django.urls import reverse

from .forms import DepositForm
from models.transaction_model import TransactionModel
from models.user_model import UserModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.http.request import HttpRequest


# Create your views here.
class DepositView(View):
    def get(self, request: "HttpRequest"):
        if not request.session.get("user_name"):
            return HttpResponseRedirect(reverse("login"))
        return render(
            request,
            "deposit.html",
            {
                "form": DepositForm(),
            },
        )

    def post(self, request: "HttpRequest"):
        user_name = request.session.get("user_name")
        if not user_name:
            return HttpResponseRedirect(reverse("login"))
        form = DepositForm(request.POST)
        if form.is_valid():
            self.handle_valid_deposit(user_name, form)
            return HttpResponseRedirect(reverse("dashboard"))
        return render(
            request,
            "deposit.html",
            {
                "form": form,
            },
        )

    def handle_valid_deposit(self, user_name: str, form: DepositForm):
        receiver = UserModel.objects.get(name=user_name)
        amount = form.cleaned_data.get("amount")
        TransactionModel.objects.create(sender=None, receiver=receiver, amount=amount)

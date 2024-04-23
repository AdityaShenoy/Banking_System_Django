from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views import View
from django.urls import reverse

from models.user_model import UserModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.http.request import HttpRequest


# Create your views here.
class TransactionsView(View):
    def get(self, request: "HttpRequest"):
        user_name = request.session.get("user_name")
        if not user_name:
            return HttpResponseRedirect(reverse("login"))
        user = UserModel.objects.get(name=user_name)
        transactions = (  # type: ignore
            user.sent_transactions.all()  # type: ignore
            .union(user.received_transactions.all())  # type: ignore
            .order_by("-time")  # type: ignore
        )
        return render(request, "transactions.html", {"transactions": transactions})

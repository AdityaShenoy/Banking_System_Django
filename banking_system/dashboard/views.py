from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views import View
from django.urls import reverse

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.http.request import HttpRequest


# Create your views here.
class DashboardView(View):
    def get(self, request: "HttpRequest"):
        if request.session.get("user_name"):
            return render(request, "dashboard.html")
        return HttpResponseRedirect(reverse("login"))

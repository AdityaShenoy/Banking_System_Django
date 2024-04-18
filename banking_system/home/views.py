from django.views import View
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.http.request import HttpRequest


# Create your views here.
class HomeView(View):
    def get(self, request: "HttpRequest"):
        return HttpResponseRedirect(reverse("login"))

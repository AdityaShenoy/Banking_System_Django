from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class HomeView(View):
    def get(self, request: HttpRequest):
        return HttpResponseRedirect(reverse("login"))

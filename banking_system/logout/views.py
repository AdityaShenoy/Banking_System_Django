from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class LogoutView(View):
    def get(self, request: HttpRequest):
        request.session.clear()
        return HttpResponseRedirect(reverse("login"))

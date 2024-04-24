from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class DashboardView(View):
    def get(self, request: HttpRequest):
        if not request.session.get("user_name"):
            return HttpResponseRedirect(reverse("login"))
        return render(request, "dashboard.html")

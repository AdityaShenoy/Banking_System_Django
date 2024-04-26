from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.views import View
from django.urls import reverse

from .forms import LoginForm
from models.user_model import UserModel
from banking_system.utils.render_form import render_form


# Create your views here.
class LoginView(View):
    def render_helper(self, request: HttpRequest, form: LoginForm):
        return render_form(request, "Send Money", "send_money", form)

    def get(self, request: HttpRequest):
        if request.session.get("user_name"):
            return HttpResponseRedirect(reverse("dashboard"))
        return self.render_helper(request, LoginForm())

    def post(self, request: HttpRequest):
        form = LoginForm(request.POST)
        if form.is_valid():
            self.handle_valid_login(request, form)
            return HttpResponseRedirect(reverse("dashboard"))
        return self.render_helper(request, form)

    def handle_valid_login(self, request: HttpRequest, form: LoginForm):
        user_name = form.cleaned_data.get("user_name")
        result = UserModel.objects.filter(name=user_name)
        if not result and user_name is not None:
            UserModel.create(name=user_name)
        request.session["user_name"] = user_name

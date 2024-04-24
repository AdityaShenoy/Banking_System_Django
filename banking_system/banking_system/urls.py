"""
URL configuration for banking_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from home.views import HomeView
from login.views import LoginView
from dashboard.views import DashboardView
from deposit.views import DepositView
from withdraw.views import WithdrawView
from send_money.views import SendMoneyView
from transactions.views import TransactionsView

app_to_class = {
    "home": HomeView,
    "login": LoginView,
    "dashboard": DashboardView,
    "deposit": DepositView,
    "withdraw": WithdrawView,
    "send_money": SendMoneyView,
    "transactions": TransactionsView,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    *[
        path(f"{app}/", class_.as_view(), name=app)
        for app, class_ in app_to_class.items()
    ],
]

from django.test import SimpleTestCase
from django.urls import reverse, resolve


from home.views import HomeView
from login.views import LoginView
from dashboard.views import DashboardView
from deposit.views import DepositView
from withdraw.views import WithdrawView
from send_money.views import SendMoneyView
from transactions.views import TransactionsView


class TestUrls(SimpleTestCase):
    def test_url_resolution(self):
        url_name_to_class = {
            "home": HomeView,
            "login": LoginView,
            "dashboard": DashboardView,
            "deposit": DepositView,
            "withdraw": WithdrawView,
            "send_money": SendMoneyView,
            "transactions": TransactionsView,
        }
        for url_name, class_ in url_name_to_class.items():
            url = reverse(url_name)
            resolved_url = resolve(url)
            self.assertEquals(resolved_url.func.view_class, class_)  # type: ignore to suppress false positive error

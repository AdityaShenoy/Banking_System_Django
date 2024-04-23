from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_without_login(self):
        after_login_apps = [
            "dashboard",
            "deposit",
            "withdraw",
            "send_money",
            "transactions",
        ]
        for url in after_login_apps:
            response = self.client.get(reverse(url))
            self.assertEquals(response.status_code, 302)

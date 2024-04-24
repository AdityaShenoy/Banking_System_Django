from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client1 = Client()

        self.client2 = Client()
        self.client2.post(reverse("login"), {"user_name": "User 1"})

        self.after_login_get_only_apps = ["dashboard", "transactions"]
        self.after_login_get_or_post_apps = [
            "deposit",
            "withdraw",
            "send_money",
        ]
        self.after_login_get_apps = (
            self.after_login_get_only_apps + self.after_login_get_or_post_apps
        )

    def test_get_and_post_without_login(self):
        for app in self.after_login_get_apps:
            response = self.client1.get(reverse(app))
            self.assertEquals(response.status_code, 302)
        for app in self.after_login_get_or_post_apps:
            response = self.client1.post(reverse(app))
            self.assertEquals(response.status_code, 302)

    def test_get_after_login(self):
        for app in self.after_login_get_apps:
            response = self.client2.get(reverse(app))
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, f"{app}.html")

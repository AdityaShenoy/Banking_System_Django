from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client1 = Client()

        self.client2 = Client()
        self.client2.post(reverse("login"), {"user_name": "User 1"})

    def test_get_without_login(self):
        after_login_apps = [
            "dashboard",
            "deposit",
            "withdraw",
            "send_money",
            "transactions",
        ]
        for app in after_login_apps:
            response = self.client1.get(reverse(app))
            self.assertEquals(response.status_code, 302)

    def test_post_invalid(self):
        apps_with_forms = ["deposit", "withdraw", "send_money"]
        for app in apps_with_forms:
            response = self.client2.post(reverse(app), {})
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, f"{app}.html")

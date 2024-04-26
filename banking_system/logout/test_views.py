from django.test import TestCase
from django.urls import reverse


class TestLogoutViews(TestCase):
    def test_get(self):
        response = self.client.post(reverse("login"), {"user_name": "User 1"})
        self.assertEquals(self.client.session.get("user_name"), "User 1")
        response = self.client.get(reverse("logout"))
        self.assertIsNone(self.client.session.get("user_name"))
        self.assertEquals(response.status_code, 302)

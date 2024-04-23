from django.test import TestCase, Client
from django.urls import reverse


class TestDashboardViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_with_login(self):
        self.client.post(reverse("login"), {"user_name": "User 1"})
        response = self.client.get(reverse("dashboard"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed("dashboard.html")

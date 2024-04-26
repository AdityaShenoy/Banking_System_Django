from django.test import TestCase, Client
from django.urls import reverse

from models.user_model import UserModel
from models.account_model import AccountModel


class TestLoginViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get(self):
        response = self.client.get(reverse("login"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "forms.html")

    def test_get_already_logged_in(self):
        client = Client()
        client.post(reverse("login"), {"user_name": "User 1"})
        response = client.get(reverse("login"))
        self.assertEquals(response.status_code, 302)

    def test_post_invalid(self):
        response = self.client.post(reverse("login"), {})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "forms.html")

    def test_post_valid_new_user(self):
        response = self.client.post(reverse("login"), {"user_name": "User 1"})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(UserModel.objects.filter(name="User 1")), 1)
        self.assertEquals(len(AccountModel.objects.filter(user__name="User 1")), 1)
        self.assertEquals(self.client.session.get("user_name"), "User 1")

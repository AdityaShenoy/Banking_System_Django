from django.test import TestCase, Client
from django.urls import reverse


class TestTransactionsViews(TestCase):
    def setUp(self):
        self.client1 = Client()
        self.client1.post(reverse("login"), {"user_name": "User 1"})
        self.client1.post(reverse("deposit"), {"amount": 100})

        self.client2 = Client()
        self.client2.post(reverse("login"), {"user_name": "User 2"})

        self.client1.post(reverse("send_money"), {"to": "User 2", "amount": 1})

    def test_get(self):
        response = self.client1.get(reverse("transactions"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "transactions.html")

    def test_get_without_login(self):
        client = Client()
        response = client.get(reverse("send_money"))
        self.assertEquals(response.status_code, 302)

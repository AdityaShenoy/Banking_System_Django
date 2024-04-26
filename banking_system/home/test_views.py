from django.test import TestCase
from django.urls import reverse


class TestHomeViews(TestCase):
    def test_get(self):
        response = self.client.get(reverse("home"))
        self.assertEquals(response.status_code, 302)

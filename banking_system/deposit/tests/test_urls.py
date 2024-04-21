from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import DepositView


class TestDepositUrls(SimpleTestCase):
    def test_url_resolution(self):
        url = reverse("deposit")
        resolved_url = resolve(url)
        # Adding ignore comment to suppress false positive error
        # Cannot access member "view_class" for type "function"
        self.assertEquals(resolved_url.func.view_class, DepositView)  # type: ignore

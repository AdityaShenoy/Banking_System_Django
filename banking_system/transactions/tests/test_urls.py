from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import TransactionsView


class TestTransactionsUrls(SimpleTestCase):
    def test_url_resolution(self):
        url = reverse("transactions")
        resolved_url = resolve(url)
        # Adding ignore comment to suppress false positive error
        # Cannot access member "view_class" for type "function"
        self.assertEquals(resolved_url.func.view_class, TransactionsView)  # type: ignore

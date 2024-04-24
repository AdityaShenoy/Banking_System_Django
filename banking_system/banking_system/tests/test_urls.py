from django.test import SimpleTestCase
from django.urls import reverse, resolve


from banking_system.urls import app_to_class


class TestUrls(SimpleTestCase):
    def test_url_resolution(self):
        for url_name, class_ in app_to_class.items():
            url = reverse(url_name)
            resolved_url = resolve(url)
            self.assertEquals(resolved_url.func.view_class, class_)  # type: ignore to suppress false positive error

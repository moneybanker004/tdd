from django.http import HttpRequest
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):
    def test_home_page_returns_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertIn("<title>To-Do</title>", html)
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</html>"))

# Create your tests here.

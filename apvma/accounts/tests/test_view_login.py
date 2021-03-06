from django.test import TestCase
from django.shortcuts import resolve_url as r


class LogInViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('login'))

    def test_get(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'login.html')

    def test_link_to_request_signup(self):
        expected = '<a href="/request_signup/"'
        self.assertContains(self.resp, expected)
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.test.client import Client
# import json
from mock.views import mock_main
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from .models import AlertSetting

class TestAlertView(TestCase):

    # call before test
    def setUp(self):
        # auto deleted after test
        self.user = User.objects.create_user(username='django_test', password='testuser')
        self.factory = RequestFactory()
        self.client  = Client()

    def test_alert_setting(self):
        self.client.login(username='django_test', password='testuser')
        response = self.client.get("/accounts/alert_settings/")
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        request = self.factory.get("/mock_main/")
        # request.user = self.user # https://docs.djangoproject.com/en/1.9/topics/testing/advanced/#example
        response = mock_main(request)
        print(response.content)
        self.assertEqual(response.status_code, 200)

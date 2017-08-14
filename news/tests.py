from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from requests.auth import HTTPBasicAuth
from django.contrib.auth.models import User
# Create your tests here.


class NewsTest(TestCase):
    def test_unauthorized_access(self):
        print("Testing Unauthorized access.")
        response = self.client.get('http://testserver/users/')
        print(response.content)
        assert response.status_code == 403

    def test_article_access(self):
        print("Testingn Articles access. ")
        url = reverse('article-list')
        response = self.client.get('http://testserver' + 'url')
        print(str(response.content))
        assert response.status_code == 200


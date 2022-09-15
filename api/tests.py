from rest_framework.test import APITestCase
from api.models import User
from rest_framework.views import status

class TokenAPITests(APITestCase):
    def test_api_read(self):
        url = "/api/token/read_product/"
        u = User.objects.create_user(username='user', email='user@foo.com', password='pass')
        resp = self.client.post(url, {'username':'user', 'password':'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
    def test_api_manage(self):
        url = "/api/token/manage_product/"
        u = User.objects.create_user(username='user', email='user@foo.com', password='pass')
        resp = self.client.post(url, {'username':'user', 'password':'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
    def test_api_read_mange(self):
        url = "/api/token/read_manage_product/"
        u = User.objects.create_user(username='user', email='user@foo.com', password='pass')
        resp = self.client.post(url, {'username':'user', 'password':'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
    def test_api_admin(self):
        url = "/api/token/admin/"
        u = User.objects.create_user(username='user', email='user@foo.com', password='pass')
        resp = self.client.post(url, {'username':'user', 'password':'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
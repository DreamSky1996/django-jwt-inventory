from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from api.models import User
from rest_framework.views import status
from django.test import Client
from product.models import Product

class ProductAPITests(APITestCase):
    def getClient(self, role):
        url = "/api/token/{}/".format(role)
        u = User.objects.create_user(username='user', email='user@foo.com', password='pass')
        resp = self.client.post(url, {'username':'user', 'password':'pass'}, format='json')
        token = resp.data['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        return client

    def test_get_all_product(self):
        url = '/api/v1/products/'
        token = self.getToken('read_product')
        my_header = {"Authorization":"Bearer {}".format(token)}
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        resp = client.get(url)
        self.assertEqual(resp.data, [])
    
    def test_get_all_product(self):
        url = '/api/v1/products/'
        client = self.getClient('read_product')
        resp = client.get(url)
        self.assertEqual(resp.data, [])
    
    def test_get_product(self):
        product = Product.objects.create(data="product-data")
        id = product.id
        url = '/api/v1/products/{}/'.format(id)
        client = self.getClient('read_product')
        resp = client.get(url)
        self.assertEqual(resp.data['id'], id)

    def test_update_product(self):
        product = Product.objects.create(data="product-data")
        id = product.id
        url = '/api/v1/products-update/{}/'.format(id)
        client = self.getClient('manage_product')
        resp = client.put(url, data={ "data":"product-data-update"})
        self.assertEqual(resp.data, {'status': 'success'})
    def test_create_product(self):
        url = '/api/v1/products-create/'
        client = self.getClient('manage_product')
        resp = client.post(url, data={ "data":"product-data-update"})
        self.assertEqual(resp.data['data'], "product-data-update")
    
    def test_delete_product(self):
        product = Product.objects.create(data="product-data")
        id = product.id
        url = '/api/v1/products-hard-del/{}/'.format(id)
        client = self.getClient('admin')
        resp = client.delete(url)
        print(resp)
        self.assertEqual(resp.data,{'status': 'success'})
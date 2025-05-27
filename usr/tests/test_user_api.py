#  test for user api

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('usr:create')

def create_user(**params):
    """creare ans rtuen new usre"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    def setup(self):
        self.client = APIClient()
        
    def test_create_user_success(self):
        payload = {
            'email' : 'test2@example.com',
            'password' : 122,
            'name' : 'yash'
        }
        
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email = payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password' , res.data)
        
    def test_user_with_email_exist_error(self):
        payload = {
            'email' :'test2@example.com',
            'password' : 122,
            'name' : 'yash'
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code , status.HTTP_400_BAD_REQUEST)
        
        
        
    # def 
from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class ModelTests(TestCase):
    def test_new_user_email_normalize(self):
        sample_emails =[
            ['test1@EXAMPLE.COM' , 'test1@example.com'],
            ['Test2@Example.com' , 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM' ,'TEST3@example.com'],
            ['test4@example.COM' ,'test4@example.com']
            
        ]
        for email, expect in sample_emails:
            user = get_user_model().objects.create_user(email=email,password='sample@123')
            self.assertEqual(user.email,expect)
            
            
    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')
            
            
    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            email= 'test@example.com',
            password='test@123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        
        
        
        
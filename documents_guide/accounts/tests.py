from django.test import TestCase
from .models import UserProfile

class UserProfileTestCase(TestCase):
    def test_create_user_profile(self):
        user = UserProfile.objects.create_user(email='test@example.com', first_name='Test', last_name='User', password='password')
        profile = UserProfile.objects.create(user=user, phone_number='1234567890', address='Test Address')

        self.assertEqual(profile.user.email, 'test@example.com')
        self.assertEqual(profile.phone_number, '1234567890')
        self.assertEqual(profile.address, 'Test Address')

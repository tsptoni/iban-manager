from django.urls import reverse
from rest_framework import status
from ibanmanager.users.models import User, USER_TYPE
from ibanmanager.utils.tests.test import BaseAPITestCase

class UserTests(BaseAPITestCase):

    def test_create_user(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('user-list')
        self.client.force_authenticate(user=self.admin_bob)
        data = {
            'username': 'user1@mail.com',
            'first_name': 'user1',
            'last_name': 'individual'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username='user1@mail.com')
        self.assertEqual(user.type, USER_TYPE.INDIVIDUAL)


    def test_modify_user_owner(self):
        url = reverse('user-detail', kwargs={'pk': self.individual_bob_owner.id})
        self.client.force_authenticate(user=self.admin_bob)
        data = {
            'first_name': 'individual modified by bob'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_modify_user_no_owner(self):
        url = reverse('user-detail', kwargs={'pk': self.individual_alice_owner.id})
        self.client.force_authenticate(user=self.admin_bob)
        data = {
            'first_name': 'individual modified by bob'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_delete_user_no_owner(self):
        url = reverse('user-detail', kwargs={'pk': self.individual_alice_owner.id})
        self.client.force_authenticate(user=self.admin_bob)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

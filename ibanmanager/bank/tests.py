from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ibanmanager.bank.models import Account
from ibanmanager.utils.tests.test import BaseAPITestCase

class AccountTests(BaseAPITestCase):

    def test_create_account_owner_bob(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        self.client.force_authenticate(user=self.admin_bob)
        data = {
            'owner': self.individual_bob_owner.id,
            'iban': 'ES79 2100 0813 6101 2345 6789'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_account_owner_bob_bad_format(self):
        url = reverse('account-list')
        self.client.force_authenticate(user=self.admin_bob)
        data = {
            'owner': self.individual_bob_owner.id,
            'iban': 'ES792100081361012300000' # Fake account
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_account_no_owner_alice(self):
        url = reverse('account-list')
        self.client.force_authenticate(user=self.admin_alice)
        data = {
            'owner': self.individual_bob_owner.id,
            'iban': 'ES79 2100 0813 6101 2345 6789'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_create_account_owner_alice(self):
        url = reverse('account-list')
        self.client.force_authenticate(user=self.admin_alice)
        data = {
            'owner': self.individual_alice_owner.id,
            'iban': 'ES79 2100 0813 6101 2345 6789'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_delete_account_owner_bob(self):
        url = reverse('account-detail', kwargs={'pk': self.account_individual_bob_owner.id})
        self.client.force_authenticate(user=self.admin_bob)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_delete_account_no_owner_bob(self):
        url = reverse('account-detail', kwargs={'pk': self.account_individual_alice_owner.id})
        self.client.force_authenticate(user=self.admin_bob)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
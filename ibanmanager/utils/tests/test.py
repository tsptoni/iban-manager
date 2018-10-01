from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ibanmanager.users.models import User, USER_TYPE
from ibanmanager.bank.models import Account


class BaseAPITestCase(APITestCase):

    def setUp(self):
        # We want to go ahead and originally create a user.
        self.admin_bob, _ = User.create_admin_user(email='admin_bob@mail.com', first_name='bob', last_name='admin')
        self.admin_alice, _ = User.create_admin_user(email='admin_alice@mail.com', first_name='alice', last_name='admin')
        self.individual_no_owner = User.objects.create_user(username='individual_no_owner@mail.com', email='individual_no_owner@mail.com', first_name='individual', last_name='no_owner')
        self.individual_bob_owner = User.objects.create_user(username='individual_bob_owner@mail.com', email='individual_bob_owner@mail.com', first_name='individual', last_name='bob_owner', created_by=self.admin_bob)
        self.individual_alice_owner = User.objects.create_user(username='individual_alice_owner@mail.com', email='individual_alice_owner@mail.com', first_name='individual', last_name='alice_owner', created_by=self.admin_alice)

        self.account_individual_bob_owner = Account.objects.create(owner=self.individual_bob_owner, iban='ES79 2100 0813 6101 2345 6789')
        self.account_individual_alice_owner = Account.objects.create(owner=self.individual_alice_owner, iban='ES79 2100 0813 6101 2345 6789')

        self.client = APIClient()


    def test_created_users(self):
        """
        Ensure we have created the users objects.
        """
        url = reverse('user-list')
        self.client.force_authenticate(user=self.admin_bob)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 5)
        self.assertEqual(User.objects.get(username='admin_bob@mail.com').email, 'admin_bob@mail.com')
        self.assertEqual(User.objects.get(username='admin_bob@mail.com').type, USER_TYPE.ADMIN)
        self.assertEqual(User.objects.get(username='admin_alice@mail.com').email, 'admin_alice@mail.com')
        self.assertEqual(User.objects.get(username='admin_alice@mail.com').type, USER_TYPE.ADMIN)
        self.assertEqual(User.objects.get(username='individual_no_owner@mail.com').email, 'individual_no_owner@mail.com')
        self.assertEqual(User.objects.get(username='individual_no_owner@mail.com').type, USER_TYPE.INDIVIDUAL)
        self.assertEqual(User.objects.get(username='individual_no_owner@mail.com').created_by, None)
        self.assertEqual(User.objects.get(username='individual_bob_owner@mail.com').email, 'individual_bob_owner@mail.com')
        self.assertEqual(User.objects.get(username='individual_bob_owner@mail.com').type, USER_TYPE.INDIVIDUAL)
        self.assertEqual(User.objects.get(username='individual_bob_owner@mail.com').created_by, self.admin_bob)
        self.assertEqual(User.objects.get(username='individual_alice_owner@mail.com').email, 'individual_alice_owner@mail.com')
        self.assertEqual(User.objects.get(username='individual_alice_owner@mail.com').type, USER_TYPE.INDIVIDUAL)
        self.assertEqual(User.objects.get(username='individual_alice_owner@mail.com').created_by, self.admin_alice)



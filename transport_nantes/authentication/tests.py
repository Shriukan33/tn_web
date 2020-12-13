from django.test import TestCase

from django.contrib.sites.models import Site
from django.conf import settings

# Create your tests here.

# TODO Test good printing of pages (first print, post, redirect) and also page needing token from mail
# TODO Test adding of new user if account doesn't exist and if account already exists
class UserTest(TestCase):

    def setUp(self):
        settings.ROLE = 'test'
        print('setup')

    def tearDown(self):
        print('teardown')

    def test_something(self):
        print(settings.ROLE)
        self.assertEqual(1 == 1, True)

import time
from django.test import TestCase
from django.contrib.auth.models import User

from models import Park

class SimpleTest(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username='user1')
        self.u2 = User.objects.create(username='user2')
        self.u3 = User.objects.create(username='user3')

    def testPark(self):
        """
        Tests the parking in a rep and its basic properties and action
        """
        p = Park.objects.create(owner=self.u1, rep=self.u2)
        self.assertTrue(p.is_current)
        p2 = Park.objects.create(owner=self.u1, rep=self.u3)
        self.assertTrue(p2.is_current)
        time.sleep(1)
        self.assertTrue(not p.is_current)


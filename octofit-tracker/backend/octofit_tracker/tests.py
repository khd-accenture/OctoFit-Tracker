from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        User.objects.create(name='Batman', email='batman@dc.com', team=dc)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 2)
        self.assertTrue(User.objects.filter(email='spiderman@marvel.com').exists())
        self.assertTrue(User.objects.filter(email='batman@dc.com').exists())

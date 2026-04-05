from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(Team.objects.count(), 1)
    def test_user_create(self):
        t = Team.objects.create(name='Test Team')
        u = User.objects.create(name='Test User', email='test@example.com', team=t)
        self.assertEqual(User.objects.count(), 1)
    def test_activity_create(self):
        t = Team.objects.create(name='Test Team')
        u = User.objects.create(name='Test User', email='test@example.com', team=t)
        a = Activity.objects.create(user=u, type='Run', duration=10, date='2026-04-05')
        self.assertEqual(Activity.objects.count(), 1)
    def test_workout_create(self):
        w = Workout.objects.create(name='Test Workout', description='desc', suggested_for='Test')
        self.assertEqual(Workout.objects.count(), 1)
    def test_leaderboard_create(self):
        t = Team.objects.create(name='Test Team')
        l = Leaderboard.objects.create(team=t, points=42)
        self.assertEqual(Leaderboard.objects.count(), 1)
